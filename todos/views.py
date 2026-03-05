from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpRequest
from .models import Todo

# Display list with active and completed todos
def list_todo_items(request):
    # Fetch from Cloud (Default)
    active_cloud = Todo.objects.filter(completed=False)
    
    # Try to fetch from Local Postgres
    try:
        active_local = Todo.objects.using('local').filter(completed=False)
        # Combine and order
        from itertools import chain
        active_todos = sorted(
            chain(active_cloud, active_local),
            key=lambda x: x.created_at,
            reverse=True
        )
    except Exception:
        # Fallback if local DB is offline or password wrong
        active_todos = active_cloud.order_by('-created_at')

    return render(request, 'todos/todo_list.html', {
        'todo_list': active_todos,
    })

# Insert new todo item
def insert_todo_item(request: HttpRequest):
    if request.method == 'POST':
        content = request.POST.get('content', '').strip()
        if content:
            Todo.objects.create(content=content)
    return redirect('todo_list')

# Helper function to find todo in either DB
def get_todo_anywhere(todo_id):
    # Try Cloud first
    todo = Todo.objects.filter(id=todo_id).first()
    if todo:
        return todo, 'default'
    # Try Local next
    try:
        todo = Todo.objects.using('local').filter(id=todo_id).first()
        if todo:
            return todo, 'local'
    except Exception:
        pass
    return None, None

# Delete a todo item
def delete_todo_item(request, todo_id):
    todo, db = get_todo_anywhere(todo_id)
    if todo:
        todo.delete(using=db)
    return redirect('todo_list')

# Edit an existing todo
def edit_todo_item(request, todo_id):
    todo, db = get_todo_anywhere(todo_id)
    if not todo:
        from django.http import Http404
        raise Http404("Task not found in any database.")

    if request.method == 'POST':
        updated_content = request.POST.get('content', '').strip()
        if updated_content:
            todo.content = updated_content
            todo.save(using=db)
        return redirect('todo_list')

    return render(request, 'todos/edit_todo.html', {'todo': todo})

# Mark a todo as done
def mark_done(request, todo_id):
    todo, db = get_todo_anywhere(todo_id)
    if todo:
        todo.completed = True
        todo.save(using=db)
    return redirect('todo_list')

# ✅ Unmark a completed task (move back to active)
def unmark_done(request, todo_id):
    todo, db = get_todo_anywhere(todo_id)
    if todo:
        todo.completed = False
        todo.save(using=db)
    return redirect('todo_list')

# ✅ Show completed tasks in separate history.html
def history(request):
    # Fetch from Cloud
    completed_cloud = Todo.objects.filter(completed=True)
    
    # Try to fetch from Local
    try:
        completed_local = Todo.objects.using('local').filter(completed=True)
        from itertools import chain
        completed_list = sorted(
            chain(completed_cloud, completed_local),
            key=lambda x: x.created_at,
            reverse=True
        )
    except Exception:
        completed_list = completed_cloud.order_by('-created_at')

    return render(request, 'todos/history.html', {'completed_list': completed_list})

# ✅ Delete all completed tasks
def delete_all_completed(request):
    Todo.objects.filter(completed=True).delete()
    return redirect('history')

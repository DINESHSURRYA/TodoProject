from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpRequest
from .models import Todo

# Display list with active and completed todos
def list_todo_items(request):
    active_todos = Todo.objects.filter(completed=False).order_by('-created_at')
    completed_todos = Todo.objects.filter(completed=True).order_by('-created_at')
    return render(request, 'todos/todo_list.html', {
        'todo_list': active_todos,
        'completed_list': completed_todos,
    })

# Insert new todo item
def insert_todo_item(request: HttpRequest):
    if request.method == 'POST':
        content = request.POST.get('content', '').strip()
        if content:
            Todo.objects.create(content=content)
    return redirect('todo_list')

# Delete a todo item
def delete_todo_item(request, todo_id):
    todo_to_delete = get_object_or_404(Todo, id=todo_id)
    todo_to_delete.delete()
    return redirect('todo_list')

# Edit an existing todo
def edit_todo_item(request, todo_id):
    todo = get_object_or_404(Todo, pk=todo_id)

    if request.method == 'POST':
        updated_content = request.POST.get('content', '').strip()
        if updated_content:
            todo.content = updated_content
            todo.save()
        return redirect('todo_list')

    return render(request, 'todos/edit_todo.html', {'todo': todo})

# Mark a todo as done
def mark_done(request, todo_id):
    todo = get_object_or_404(Todo, id=todo_id)
    todo.completed = True
    todo.save()
    return redirect('todo_list')

# ✅ Unmark a completed task (move back to active)
def unmark_done(request, todo_id):
    todo = get_object_or_404(Todo, id=todo_id)
    todo.completed = False
    todo.save()
    return redirect('todo_list')

# ✅ Show completed tasks in separate history.html
def history(request):
    completed_list = Todo.objects.filter(completed=True).order_by('-created_at')
    return render(request, 'todos/history.html', {'completed_list': completed_list})

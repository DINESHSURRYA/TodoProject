from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.list_todo_items, name='todo_list'),
    path('insert/', views.insert_todo_item, name='insert_todo_item'),
    path('edit_todo/<int:todo_id>/', views.edit_todo_item, name='edit_todo_item'),
    path('delete/<int:todo_id>/', views.delete_todo_item, name='delete_todo_item'),
    path('mark_done/<int:todo_id>/', views.mark_done, name='mark_done'),
    path('unmark_done/<int:todo_id>/', views.unmark_done, name='unmark_done'),  # ✅ REQUIRED
    path('history/', views.history, name='history'),  # ✅ Add this line
    path('delete_all_completed/', views.delete_all_completed, name='delete_all_completed'),
]



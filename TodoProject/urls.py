from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    path('', lambda request: redirect('todo_list')),  # 🔁 Now matches name='todo_list'
    path('admin/', admin.site.urls),
    path('todos/', include('todos.urls')),
]

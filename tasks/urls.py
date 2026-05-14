from django.urls import path
from .views import create_task, edit_task

urlpatterns = [
  path('task/create/', create_task, name='create_task'),
  path('task/edit/<int:task_id>/', edit_task, name='edit_task')
]
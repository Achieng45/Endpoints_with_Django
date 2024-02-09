from django.urls import path
from . import views

urlpatterns = [
    path('tasks/', views.task_list, name='task_list'),
    path('task/<int:pk>/', views.task_detail, name='task_detail'),
    path('task/<int:task_id>/status/', views.update_task_status, name='update_task_status'),
    path('tasks/<str:status>/', views.get_tasks_by_status, name='get_tasks_by_status'),
    path('tasks/delete', views.delete_all_tasks, name='delete_all_tasks'),
    path('task/<int:pk>/', views.delete_task_by_id, name='delete_task_by_id'),
]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),

    #task
    path('tasks/', views.TaskView.as_view(), name='task'),
    path('tasks/create', views.TaskCreateView.as_view(), name='task-create'),
    path('tasks/<pk>/edit', views.TaskUpdateView.as_view(), name='task-edit'),
    path('tasks/<pk>/delete', views.TaskDeleteView.as_view(), name='task-delete'),

    #task-list
    path('tasks/create-list', views.TaskListCreateView.as_view(), name='task-list-create'),
    path('tasks/<pk>/edit-list', views.TaskListUpdateView.as_view(), name='task-list-edit'),
    path('tasks/<pk>/delete-list', views.TaskListDeleteView.as_view(), name='task-list-delete'),
    
    #tag
    path('tasks/create-tag', views.TagCreateView.as_view(), name='tag-create'),
    path('tasks/<pk>/edit-tag', views.TagUpdateView.as_view(), name='tag-edit'),
    path('tasks/<pk>/delete-tag', views.TagDeleteView.as_view(), name='tag-delete'),
]
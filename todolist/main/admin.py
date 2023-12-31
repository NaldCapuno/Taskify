from django.contrib import admin
from . import models

@admin.register(models.Priority)
class PriorityAdmin(admin.ModelAdmin):
    list_display = ('name', 'level', 'created_at', 'updated_at',)

@admin.register(models.Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'created_at', 'updated_at',)

@admin.register(models.TaskList)
class TaskListAdmin(admin.ModelAdmin):
    list_display = ('user', 'title', 'created_at', 'updated_at',)

@admin.register(models.Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('user', 'title', 'task_list', 'description', 'due_date', 'completed', 'created_at', 'updated_at',)
    list_filter = ('task_list', 'completed', 'tag',)
    search_fields = ('task_list', 'title',)
from django import forms
from django.contrib.auth.models import User
from . import models

class TagCreateForm(forms.ModelForm):
    class Meta:
        model = models.Tag
        fields = '__all__'

class TaskListCreateForm(forms.ModelForm):
    class Meta:
        model = models.TaskList
        fields = '__all__'

class TaskCreateForm(forms.ModelForm):
    due_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), required=False)
    class Meta:
        model = models.Task
        fields = ('user', 'title', 'task_list', 'description', 'due_date', 'priority', 'tag', 'completed')
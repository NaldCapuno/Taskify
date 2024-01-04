from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy
from . import forms, models

class HomeView(ListView):
    def get(self, request):
        return render(request, 'home.html', {})

class TaskView(ListView):
    model = models.TaskList
    template_name = 'task.html'
    paginate_by = 3
    context_object_name = 'task_list'

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return models.TaskList.objects.filter(user=self.request.user)
        else:
            return models.TaskList.objects.none()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            context['tasks'] = models.Task.objects.filter(user=self.request.user)
            context['tags'] = models.Tag.objects.filter(user=self.request.user)
        return context

# TASK
class TaskCreateView(CreateView):
    template_name = 'CRUD/task-create.html'
    form_class = forms.TaskCreateForm

    def get(self, request, task_list_id, *args, **kwargs):
        task_list = models.TaskList.objects.get(id=task_list_id)
        form = self.form_class(initial={'user': request.user, 'task_list': task_list})
        form.fields['user'].queryset = User.objects.filter(id=request.user.id)
        form.fields['task_list'].queryset = models.TaskList.objects.filter(user=request.user)
        form.fields['tag'].queryset = models.Tag.objects.filter(user=request.user)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task')
        return render(request, self.template_name, {'form': form})
    
class TaskUpdateView(UpdateView):
    model = models.Task
    template_name = 'CRUD/task-edit.html'
    form_class = forms.TaskCreateForm
    success_url = reverse_lazy('task')

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['user'].queryset = models.User.objects.filter(id=self.request.user.id)
        form.fields['tag'].queryset = models.Tag.objects.filter(user=self.request.user)
        return form

class TaskDeleteView(DeleteView):
    model = models.Task
    template_name = 'CRUD/task-delete.html'
    success_url = reverse_lazy('task')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['task_title'] = self.object.title
        return context

# TASK LIST
class TaskListCreateView(CreateView):
    template_name = 'CRUD/task-list-create.html'
    form_class = forms.TaskListCreateForm

    def get(self, request):
        form = self.form_class(initial={'user': request.user})
        form.fields['user'].queryset = User.objects.filter(id=request.user.id)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task')
        return render(request, self.template_name, {'form': form})

class TaskListUpdateView(UpdateView):
    model = models.TaskList
    template_name = 'CRUD/task-list-edit.html'
    form_class = forms.TaskListCreateForm
    success_url = reverse_lazy('task')

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['user'].queryset = models.User.objects.filter(id=self.request.user.id)
        return form

class TaskListDeleteView(DeleteView):
    model = models.TaskList
    template_name = 'CRUD/task-list-delete.html'
    success_url = reverse_lazy('task')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['task_list_title'] = self.object.title
        return context

# TAG
class TagCreateView(CreateView):
    template_name = 'CRUD/tag-create.html'
    form_class = forms.TagCreateForm

    def get(self, request):
        form = self.form_class(initial={'user': request.user})
        form.fields['user'].queryset = User.objects.filter(id=request.user.id)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task')
        return render(request, self.template_name, {'form': form})
    
class TagUpdateView(UpdateView):
    model = models.Tag
    template_name = 'CRUD/tag-edit.html'
    form_class = forms.TagCreateForm
    success_url = reverse_lazy('task')

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['user'].queryset = models.User.objects.filter(id=self.request.user.id)
        return form

class TagDeleteView(DeleteView):
    model = models.Tag
    template_name = 'CRUD/tag-delete.html'
    success_url = reverse_lazy('task')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tag_name'] = self.object.name
        return context
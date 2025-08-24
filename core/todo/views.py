from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Task
from django.views.generic.list import ListView
from .forms import TaskUpdateForm
from django.urls import reverse_lazy
from django.views import View
from django.shortcuts import redirect
from accounts.models import CustomUser
from django.views.generic.edit import (
    CreateView,
    DeleteView,
    UpdateView,
)

class TaskList(LoginRequiredMixin, ListView):
    # show task list
    model = Task
    template_name = 'todo/list_task.html'
    context_object_name = 'tasks'

    # def get_queryset(self):
    #     return super().get_queryset(user=self.request.user)

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)

class TaskCreate(LoginRequiredMixin, CreateView):
    model = Task
    fields = ["title"]
    success_url = reverse_lazy('todo:task_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TaskCreate, self).form_valid(form)

class TaskUpdate(LoginRequiredMixin, UpdateView):
    model = Task
    form_class = TaskUpdateForm
    template_name = 'todo/update_task.html'
    success_url = reverse_lazy('todo:task_list')

class TaskComplete(LoginRequiredMixin, View):
    model = Task
    success_url = reverse_lazy('todo:task_list')

    def get(self, request, *args, **kwargs):
        object = Task.objects.get(id=kwargs.get("pk"))
        object.complete = True
        object.save()
        return redirect(self.success_url)

class DeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    success_url = reverse_lazy('todo:task_list')
    context_object_name = 'task'

    def get(self, request, *args, **kwargs):
        object = Task.objects.get(id=kwargs.get("pk"))
        object.delete()
        return redirect(self.success_url)

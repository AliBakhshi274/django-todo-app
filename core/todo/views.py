from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import TaskUpdateForm
from .models import Task
from django.views.generic.list import ListView

class TaskList(LoginRequiredMixin, ListView):
    # show task list
    model = Task
    template_name = 'todo/list_task.html'
    context_object_name = 'tasks'

    # def get_queryset(self):
    #     return super().get_queryset(user=self.request.user)

    

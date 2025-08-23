from django.urls import path
from todo.views import TaskListView

app_name = "todo"

urlpatterns = [
    path('', TaskListView, name='task_list'),
]
from django.urls import path
from todo.views import TaskList

app_name = "todo"

urlpatterns = [
    path('', TaskList.as_view(), name='task_list'),
    path('create/', TaskCreate.as_view(), name='create_task'),
    path('update/<int:pk>', TaskUpdate.as_view(), name='update_task'),
    path('delete/<int:pk>', TaskDelete.as_view(), name='delete_task'),
    path('complete/<int:pk>', TaskCompelete.as_view(), name='complete_task'),
]
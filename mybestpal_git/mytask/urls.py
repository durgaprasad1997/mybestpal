
from django.urls import path
from mytask.views.my_task import *

app_name="mytask"

urlpatterns=[

    path(r'addtask/<int:user_id>/', AddTaskView.as_view(), name="addtask"),
    path(r'updatetask/<int:pk>/', UpdateTask.as_view(), name="updatetask"),
    path(r'deletetask/<int:pk>/', DeleteTask.as_view(), name="deletetask"),
    path(r'tasklist/', Viewtasklist.as_view(), name="tasklist"),


]


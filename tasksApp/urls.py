from django.urls import path
from tasksApp import views
from .views import createTask, deleteTask

urlpatterns = [
        path('', views.task, name="Task"),
        path('new/', createTask, name='createTask'),
        path('delete/<int:id>/', deleteTask, name='deleteTask'),
]

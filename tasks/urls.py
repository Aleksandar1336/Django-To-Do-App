# tasks/urls.py

from django.urls import path
from .views import (
    HomeView,
    SignUpView,
    TaskListView,
    TaskCreateView,
    TaskDetailView,
    TaskUpdateView,
    TaskDeleteView,
    ToggleTaskView,
)

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("signup/", SignUpView.as_view(), name="signup"),
    path("tasks/", TaskListView.as_view(), name="task_list"),
    path("tasks/add/", TaskCreateView.as_view(), name="add_task"),
    path("tasks/<int:pk>/", TaskDetailView.as_view(), name="task_detail"),
    path("tasks/<int:pk>/edit/", TaskUpdateView.as_view(), name="edit_task"),
    path("tasks/<int:pk>/delete/", TaskDeleteView.as_view(), name="delete_task"),
    path("toggle/<int:pk>/", ToggleTaskView.as_view(), name="toggle_task"),
]

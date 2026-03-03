from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("tasks/", views.task_list, name="task_list"),
    path("tasks/add/", views.add_task, name="add_task"),
    path("tasks/<int:pk>/", views.task_detail, name="task_detail"),
    path("tasks/<int:pk>/edit/", views.edit_task, name="edit_task"),
    path("tasks/<int:pk>/delete/", views.delete_task, name="delete_task"),
    path("toggle/<int:pk>/", views.toggle_task, name="toggle_task"),
    # Signup
    path("signup/", views.signup, name="signup"),
]

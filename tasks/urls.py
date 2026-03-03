from django.urls import path
from . import views

urlpatterns = [
    path("", views.task_list, name="task_list"),
    path("add/", views.add_task, name="add_task"),
    path("<int:pk>/", views.task_detail, name="task_detail"),
    path("<int:pk>/edit/", views.edit_task, name="edit_task"),
    path("<int:pk>/delete/", views.delete_task, name="delete_task"),
    # Signup
    path("signup/", views.signup, name="signup"),
]

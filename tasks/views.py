# tasks/views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import (
    TemplateView,
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
    DetailView,
)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .models import Task
from .forms import TaskForm


# ------------------------
# Home View
# ------------------------
class HomeView(TemplateView):
    template_name = "home.html"


# ------------------------
# Signup View
# ------------------------
class SignUpView(View):
    def get(self, request):
        form = UserCreationForm()
        return render(request, "registration/signup.html", {"form": form})

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("task_list")
        return render(request, "registration/signup.html", {"form": form})


# ------------------------
# Task List + Create (Combined)
# ------------------------
class TaskListView(LoginRequiredMixin, ListView):
    model = Task
    template_name = "task_list.html"
    context_object_name = "tasks"
    login_url = "login"

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user).order_by("-id")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = TaskForm()
        return context

    def post(self, request, *args, **kwargs):
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
        return redirect("task_list")


# ------------------------
# Separate Create View (Optional)
# ------------------------
class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    form_class = TaskForm
    template_name = "add_task.html"
    success_url = reverse_lazy("task_list")
    login_url = "login"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


# ------------------------
# Task Detail
# ------------------------
class TaskDetailView(LoginRequiredMixin, DetailView):
    model = Task
    template_name = "task_detail.html"
    context_object_name = "task"
    login_url = "login"

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)


# ------------------------
# Task Update
# ------------------------
class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model = Task
    fields = ["title", "description", "completed"]
    template_name = "edit_task.html"
    success_url = reverse_lazy("task_list")
    login_url = "login"

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)


# ------------------------
# Task Delete
# ------------------------
class TaskDeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    success_url = reverse_lazy("task_list")
    login_url = "login"

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)

    # If you don't want confirmation page
    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)


# ------------------------
# Toggle Task
# ------------------------
class ToggleTaskView(LoginRequiredMixin, View):
    login_url = "login"

    def post(self, request, pk):
        task = get_object_or_404(Task, pk=pk, user=request.user)
        task.completed = not task.completed
        task.save()
        return redirect("task_list")

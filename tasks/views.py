from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login


def signup(request):
    # Redirect authenticated users away from signup page
    if request.user.is_authenticated:
        return redirect("task_list")

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("task_list")
    else:
        form = UserCreationForm()

    return render(request, "registration/signup.html", {"form": form})


@login_required
def task_list(request):
    tasks = Task.objects.filter(user=request.user)
    return render(request, "task_list.html", {"tasks": tasks})


@login_required
def add_task(request):
    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description")
        Task.objects.create(title=title, description=description, user=request.user)
        return redirect("task_list")
    return render(request, "add_task.html")


@login_required
def task_detail(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)
    return render(request, "task_detail.html", {"task": task})


@login_required
def edit_task(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)
    if request.method == "POST":
        task.title = request.POST.get("title")
        task.description = request.POST.get("description")
        task.completed = "completed" in request.POST
        task.save()
        return redirect("task_list")
    return render(request, "edit_task.html", {"task": task})


@login_required
def delete_task(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)
    if request.method == "POST":
        task.delete()
        return redirect("task_list")
    return render(request, "delete_task.html", {"task": task})

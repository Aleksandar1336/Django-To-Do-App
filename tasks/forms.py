# tasks/forms.py
from django import forms
from .models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["title", "description"]  # Include description
        widgets = {
            "title": forms.TextInput(
                attrs={"placeholder": "Add your task here", "id": "input-box"}
            ),
            "description": forms.Textarea(
                attrs={"placeholder": "Task details", "rows": 2}
            ),
        }

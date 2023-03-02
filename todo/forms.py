from django import forms

from .models import Tasks


class TasksModelForm(forms.ModelForm):
    """Задача"""

    class Meta:
        model = Tasks
        fields = ["title"]

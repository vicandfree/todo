from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.utils import timezone
from django.views.generic import CreateView, DeleteView, ListView, View

from .forms import TasksModelForm
from .models import Tasks


class TasksListView(ListView):
    """Список задач"""

    model = Tasks
    template_name = "todo/list.html"


class TasksActiveListView(View):
    """Список задач"""

    @staticmethod
    def get(request):
        return render(request, "todo/list.html", {
            "tasks_list": Tasks.objects.filter(is_active=True).all()
        })


class TasksCreateView(CreateView):
    """Создание задачи"""

    template_name = "todo/create.html"
    form_class = TasksModelForm
    success_url = reverse_lazy("todo:index")


class TasksUpdateIsDoneView(View):
    """Редактирование статуса задачи"""

    @staticmethod
    def post(request, pk):
        item = Tasks.objects.filter(id=pk).first()
        if item.is_active:
            Tasks.objects.filter(id=pk).update(is_active=False, completed_at=timezone.now())
        else:
            Tasks.objects.filter(id=pk).update(is_active=True, completed_at=None)
        return redirect("todo:index")


class TasksDeleteView(DeleteView):
    """Удаление задачи"""

    model = Tasks
    template_name = "todo/delete.html"
    success_url = reverse_lazy("todo:index")

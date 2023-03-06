from django_filters import rest_framework as filters
from rest_framework import viewsets
from rest_framework.filters import OrderingFilter, SearchFilter

from todo.models import Tasks

from .serializer import TasksSerializer


class TasksFilter(filters.FilterSet):
    class Meta:
        model = Tasks
        fields = ("title", "is_active")


class TasksViewSet(viewsets.ModelViewSet):
    serializer_class = TasksSerializer
    queryset = Tasks.objects.all()
    filter_backends = (OrderingFilter, filters.DjangoFilterBackend, SearchFilter)
    filterset_class = TasksFilter
    ordering_fields = ["title", "is_active", "completed_at"]
    search_fields = ["$title"]

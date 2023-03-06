from django.urls import include, path

from todo.views import (
    TasksCreateView,
    TasksDeleteView,
    TasksListView,
    TasksUpdateIsDoneView,
    TasksActiveListView
)

app_name = "todo"

urlpatterns = [
    path("", TasksListView.as_view(), name="index"),
    path("active", TasksActiveListView.as_view(), name="active"),
    path("create", TasksCreateView.as_view(), name="create"),
    path("update/<int:pk>", TasksUpdateIsDoneView.as_view(), name="update"),
    path("delete/<int:pk>", TasksDeleteView.as_view(), name="delete"),
    path("api/", include("todo.api.urls")),
]

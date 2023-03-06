from django.urls import include, path

urlpatterns = [
    path("v1/", include("todo.api.v1.urls")),
]

from rest_framework import serializers

from todo.models import Tasks


class TasksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tasks
        fields = ("id", "title", "is_active", "created_at", "completed_at")

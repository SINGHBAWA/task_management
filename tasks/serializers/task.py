from django.db import models
from rest_framework import serializers
from rest_framework.fields import ReadOnlyField
from tasks.models import Task

class TaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = "__all__"
        read_only_fields = ("assigned_to", )

class TaskAssignedToSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = ("id", "assigned_to",)

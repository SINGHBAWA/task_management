from django.db import models
from django.contrib.auth import get_user_model
from tasks.choices import TaskStatus


class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=255, null=True, blank=True)
    task_date = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=30, choices=TaskStatus.CHOICES, default=TaskStatus.pending)
    assigned_to = models.ForeignKey(get_user_model(), null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

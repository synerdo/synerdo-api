from django.db import models
from users.models import CustomUser
from rooms.models import Room

# Create your models here.
class Task(models.Model):
    class Priority(models.TextChoices):
        LOW = 'L', 'Low'
        MEDIUM = 'M', 'Medium'
        HIGH = 'H', 'High'

    title = models.CharField(blank=False, max_length=150)
    text = models.CharField(blank=True, null=True)
    is_done = models.BooleanField(blank=False, default=False)
    due_to_date = models.DateField(blank=True, null=True)
    due_to_time = models.TimeField(blank=True, null=True)
    priority = models.CharField(max_length=1, choices=Priority.choices, blank=True, null=True)
    creator = models.ForeignKey(
        CustomUser,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="%(app_label)s_%(class)s_creator")
    executor = models.ForeignKey(
        CustomUser,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="%(app_label)s_%(class)s_executor")
    room = models.ForeignKey(Room, on_delete=models.SET_NULL, blank=True, null=True)


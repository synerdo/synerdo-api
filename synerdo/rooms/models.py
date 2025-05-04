from django.db import models
from users.models import CustomUser

# Create your models here.
class Room(models.Model):
    name = models.CharField(max_length=150, blank=False)
    owner = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, blank=True, null=True)
    access_code = models.CharField(max_length=22, blank=False, unique=True)


class RoomUser(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, blank=False, null=False)
    room = models.ForeignKey(Room, on_delete=models.CASCADE, blank=False, null=False)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user', 'room'], name='unique_user_room')
        ]


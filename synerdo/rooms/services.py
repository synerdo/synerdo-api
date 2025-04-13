import uuid
import base64
from rest_framework.exceptions import ValidationError

from .models import RoomUser


def gen_code():
    code = base64.urlsafe_b64encode(uuid.uuid4().bytes).decode().rstrip("=")

    return code


def exit_room(room, user):
    try:
        RoomUser.objects.get(room=room, user=user).delete()
    except RoomUser.DoesNotExist:
        raise ValidationError()

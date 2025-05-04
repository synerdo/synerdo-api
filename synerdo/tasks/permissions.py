from rest_framework import permissions
from rooms.models import RoomUser


class IsInRoom(permissions.BasePermission):
    def has_permission(self, request, view):
        room_id = view.kwargs.get('room_id')
        user = request.user
        return RoomUser.objects.filter(user=user, room_id=room_id).exists()

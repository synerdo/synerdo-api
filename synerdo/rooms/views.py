from rest_framework import generics, mixins, permissions, viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drf_spectacular.utils import extend_schema

from .serializers import RoomSerializer, RoomUserSerializer
from .models import Room, RoomUser
from .permissions import IsOwner
from .services import exit_room

from tasks.permissions import IsInRoom
from users.serializers import UserSerializer
from users.models import CustomUser


# Create your views here.
class RoomViewMixin():
    serializer_class = RoomSerializer

    def get_queryset(self):
        rooms = RoomUser.objects.filter(user=self.request.user).values_list('room', flat=True)
        return Room.objects.filter(id__in=rooms)


class RoomListCreateView(RoomViewMixin, generics.ListCreateAPIView):
    pass


class RoomRetrieveUpdateDestroyView(RoomViewMixin, mixins.UpdateModelMixin, generics.RetrieveDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated, IsOwner]

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)


class RoomUserView(mixins.CreateModelMixin, generics.GenericAPIView):
    serializer_class = RoomUserSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class RoomExitView(APIView):
    def post(self, request, pk):
        
        exit_room(room=pk, user=request.user)

        return Response(status=status.HTTP_204_NO_CONTENT)


@extend_schema(tags=['users'])
class RoomUsersViewSet(mixins.ListModelMixin,
                    mixins.RetrieveModelMixin,
                    viewsets.GenericViewSet):
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated, IsInRoom]

    '''
    def get_queryset(self):
        room_id = self.kwargs.get('room_id')
        users = RoomUser.objects.filter(room_id=room_id).values_list('user', flat=True)
        return CustomUser.objects.filter(id__in=users)
    '''

    def get_queryset(self):
        room_id = self.kwargs.get('room_id')
        return CustomUser.objects.filter(roomuser__room_id=room_id)


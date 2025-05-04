from rest_framework import generics, mixins, permissions, viewsets
from drf_spectacular.utils import extend_schema

from .models import Task
from .serializers import TaskSerializer
from .permissions import IsInRoom


@extend_schema(tags=['tasks'])
class TaskViewSet(mixins.CreateModelMixin,
                  mixins.ListModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin,
                  viewsets.GenericViewSet):
    
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated, IsInRoom]
    
    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['room_id'] = self.kwargs.get('room_id')
        return context
    
    def get_queryset(self):
        room_id = self.kwargs.get('room_id')
        return Task.objects.filter(room_id=room_id)
    


from rest_framework import serializers
from .models import Task
from rooms.models import Room


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'
        read_only_fields = ['id', 'creator', 'executor', 'room']
    
    def validate(self, attrs):
        room_id = self.context.get('room_id')

        try:
            room = Room.objects.get(id=room_id)
        except Room.DoesNotExist:
            raise serializers.ValidationError('Invalid room_id')

        attrs['room'] = room
        
        return attrs
    
    def create(self, validated_data):
        validated_data['creator'] = self.context['request'].user

        return Task.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        if 'is_done' in validated_data:
            if validated_data['is_done'] != instance.is_done:
                validated_data['executor'] = self.context['request'].user if validated_data['is_done'] else None

        return super().update(instance, validated_data)

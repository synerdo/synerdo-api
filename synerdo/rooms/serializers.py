from rest_framework import serializers
from .models import Room, RoomUser
from .services import gen_code


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ['id', 'name', 'owner', 'access_code']
        read_only_fields = ['id', 'owner', 'access_code']
    
    def create(self, validated_data):
        user = self.context['request'].user
        validated_data['owner'] = user
        validated_data['access_code'] = gen_code()

        room = Room.objects.create(**validated_data)      
        RoomUser.objects.create(user=user, room=room)

        return room


class RoomUserSerializer(serializers.ModelSerializer):
    access_code = serializers.CharField(write_only=True)

    class Meta:
        model = RoomUser
        fields = ['user', 'room', 'access_code']
        read_only_fields = ['user', 'room']
    
    def validate(self, attrs):
        user = self.context['request'].user
        attrs['user'] = user
        code = attrs['access_code']

        try:
            room = Room.objects.get(access_code=code)
        except Room.DoesNotExist:
            raise serializers.ValidationError({'access_code': 'Room not found'})

        attrs['room'] = room
        attrs.pop('access_code')

        if RoomUser.objects.filter(user=user, room=room).exists():
            raise serializers.ValidationError("User is already in this room")
        
        return attrs

    def create(self, validated_data):
        return RoomUser.objects.create(**validated_data)


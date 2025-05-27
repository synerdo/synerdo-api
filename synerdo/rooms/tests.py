from rest_framework.test import APITestCase
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from users.models import CustomUser
from .models import Room

# Create your tests here.
class RoomAPITestCase(APITestCase):
    def setUp(self):
        self.user = CustomUser.objects.create_user(username='testuser', password='q1029384756', email='testuser@gmail.com')
        
        # Получаем токен
        refresh = RefreshToken.for_user(self.user)
        self.token = str(refresh.access_token)

        # Добавляем токен в заголовок авторизации
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token)

        self.room_data = {
            'name': 'Test room',
        }

    def test_create_room(self):
        response = self.client.post('/api/rooms/', self.room_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Room.objects.count(), 1)
        self.assertEqual(Room.objects.first().name, 'Test room')
    
    def test_get_room_list(self):
        self.client.post('/api/rooms/', self.room_data)
        response = self.client.get('/api/rooms/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
    
    def test_delete_room(self):
        room = self.client.post('/api/rooms/', self.room_data)
        response = self.client.delete(f'/api/rooms/{room.data['id']}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Room.objects.count(), 0)

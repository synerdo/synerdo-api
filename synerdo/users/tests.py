from rest_framework.test import APITestCase, APIRequestFactory
from rest_framework import status
from django.urls import reverse
from .models import CustomUser
from rest_framework_simplejwt.tokens import RefreshToken

from unittest.mock import patch, MagicMock
from django.contrib.auth import get_user_model
from rest_framework.test import force_authenticate
from .views import UserView

class UserIntegrationTests(APITestCase):
    def setUp(self):
        self.register_url = reverse('register')
        self.user_view_url = reverse('user')
        self.token_url = reverse('token_obtain_pair')

        self.user_data = {
            'username': 'testuser',
            'email': 'test@example.com',
            'password': 'StrongPass123!'
        }

    def test_register_user(self):
        response = self.client.post(self.register_url, self.user_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(CustomUser.objects.filter(username='testuser').exists())

    def test_token_obtain(self):
        CustomUser.objects.create_user(**self.user_data)
        response = self.client.post(self.token_url, {
            'username': self.user_data['username'],
            'password': self.user_data['password']
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access', response.data)
        self.assertIn('refresh', response.data)

    def test_user_view_authenticated(self):
        user = CustomUser.objects.create_user(**self.user_data)
        token = RefreshToken.for_user(user).access_token
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')
        response = self.client.get(self.user_view_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['username'], user.username)

    def test_user_view_unauthenticated(self):
        response = self.client.get(self.user_view_url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)



class UserMeIntegrationTest(APITestCase):
    def setUp(self):
        self.user = CustomUser.objects.create_user(
            username='testuser', email='testuserjohn@example.com', password='StrongPass123!'
        )
        self.token = str(RefreshToken.for_user(self.user).access_token)
        self.url = reverse('user')  # предполагаем, что это api/users/me с именем "user"

    def test_get_me_authenticated(self):
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token}')
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['username'], 'testuser')

User = get_user_model()

class UserMeMockedTest(APITestCase):
    def setUp(self):
        self.factory = APIRequestFactory()

    @patch('users.views.UserView.get_object')  # Замени на путь к твоему views.py
    def test_get_me_with_force_authenticate(self, mock_get_object):
        mock_user = MagicMock(spec=User)
        mock_user.username = 'mockuser'
        mock_user.email = 'mock@example.com'
        mock_user.date_joined = '2025-01-01T00:00:00Z'
        mock_user.id = 999

        mock_get_object.return_value = mock_user

        request = self.factory.get('/api/users/me/')
        force_authenticate(request, user=mock_user)

        view = UserView.as_view()
        response = view(request)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['username'], 'mockuser')

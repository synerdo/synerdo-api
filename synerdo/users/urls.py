from django.urls import path
from .views import RegisterView, UserView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('api/auth/register/', RegisterView.as_view(), name='register'),
    path('api/auth/token/', TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path('api/auth/token/refresh/', TokenRefreshView.as_view(), name="token_refresh"),
    path('api/users/me', UserView.as_view(), name='user')
]

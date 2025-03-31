from django.urls import path
from .views import RegisterView, AccessTest
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

urlpatterns = [
    path('api/auth/register/', RegisterView.as_view(), name='register'),
    path('api/auth/token/', TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path('api/auth/token/refresh/', TokenRefreshView.as_view(), name="token_refresh"),
    path('api/auth/token/verify/', TokenVerifyView.as_view(), name="token_verify"),
    path('api/accesstest/', AccessTest.as_view(), name='access_test'),
]

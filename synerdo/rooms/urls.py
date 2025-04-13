from django.urls import path

from rooms import views


urlpatterns = [
    path('api/rooms/', views.RoomListCreateView.as_view()),
    path('api/rooms/join/', views.RoomUserView.as_view()),
    path('api/rooms/<int:pk>/', views.RoomRetrieveUpdateDestroyView.as_view()),
    path('api/rooms/<int:pk>/exit/', views.RoomExitView.as_view()),
]


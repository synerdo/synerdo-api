from django.urls import path
from tasks import views

'''
urlpatterns = [
    path('api/rooms/<int:room_id>/tasks/', views.TaskView.as_view()),
    path('api/rooms/<int:room_id>/tasks/<int:pk>/', views.TaskView.as_view()),
]
'''

task_list = views.TaskViewSet.as_view({
    'post': 'create',
    'get': 'list',
})

task_detail = views.TaskViewSet.as_view({
    'get': 'retrieve',
    'patch': 'partial_update',
    'delete': 'destroy',
})

urlpatterns = [
    path('api/rooms/<int:room_id>/tasks/', task_list),
    path('api/rooms/<int:room_id>/tasks/<int:pk>/', task_detail),
]

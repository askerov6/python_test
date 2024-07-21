from django.urls import path
from .views import HotelViewSet, RoomViewSet

urlpatterns = [
    path('', HotelViewSet.as_view({'get': 'list', 'post': 'create'}), name='hotel_name'),
    path('<int:pk>/', HotelViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='hotel_detail'),
    path('room/', RoomViewSet.as_view({'get': 'list', 'post': 'create'}), name='room_list'),
    path('room/<int:pk>/', RoomViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='room_detail'),
]

from django_filters import FilterSet
from .models import Room


class RoomFilter(FilterSet):
    class Meta:
        model = Room
        fields = {
            'hotel': ['exact'],
            'price': ['gt', 'lt'],
        }






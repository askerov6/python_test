from os import name

from django.db import models
from django.contrib.auth.models import User
from django.db.models import CharField


class Hotel(models.Model):
    objects = None
    name_hotel = models.CharField(max_length=32)
    description = models.TextField()
    addres = models.CharField(max_length=32)
    city = models.CharField(max_length=32, verbose_name="Город")
    country = models.CharField(max_length=32)

    def __str__(self):
        return f'{self.name_hotel} - {self.country}'


class HotelImage(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    hotel_image = models.ImageField(upload_to='hotel_image/')


class Room(models.Model):
    objects = None
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    room_number = models.SmallIntegerField(default=0)
    capacity = models.SmallIntegerField(default=0)
    price = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.room_number}'


class ImageRoom(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    room_image = models.ImageField(upload_to='room_image/')


class Booking(models.Model):
    user = models.CharField(max_length=32)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    chekin_in_date = models.DateTimeField()
    chekin_out_date = models.DateTimeField()
    total_price = models.PositiveIntegerField(default=0)
    STATUS_CHOICES = (
        ('Бронь', 'Бронь'),
        ('Свободный', 'Свободный'),
        ['Занять', 'Занять']
    )

 


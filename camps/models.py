from django.db import models
from django.contrib.auth.models import User


class Camps(models.Model):
    id = models.AutoField(
        primary_key=True,
        help_text='Unique ID of the camp',
    )
    lat = models.CharField(
        max_length=20,
        help_text='Latitude',
    )
    lng = models.CharField(
        max_length=20,
        help_text='Longitude',
    )
    location = models.CharField(
        max_length=60,
        help_text='Location name',
    )

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        db_column='user',
    )

    incharge = models.CharField(
        max_length=40,
        help_text='Camp incharge',
    )
    phone = models.CharField(
        max_length=15,
        help_text='Camp phone number'
    )

    photo = models.ImageField(
        blank=True,
        null=True,
        upload_to='camps/%Y/%m/%d/'
    )

    capacity = models.IntegerField(
        help_text='The max capacity of the camp'
    )
    number_of_people = models.IntegerField(
        default=0,
        help_text='The number of people currently in the camp'
    )

    def __str__(self):
        return self.location

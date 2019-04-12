from django.db import models


class GeoCoordinates(models.Model):

    city = models.CharField(max_length=50, null=False)
    country = models.CharField(max_length=50, null=False)
    latitude = models.FloatField(null=False)
    longitude = models.FloatField(null=False)
    date_pub = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.country} - {self.city}'


class InstagramUsers(models.Model):
    username = models.CharField(max_length=30, null=False)
    password = models.CharField(max_length=30, null=False)
    date_pub = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.username} - {self.password}'




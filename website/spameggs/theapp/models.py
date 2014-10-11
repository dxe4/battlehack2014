from django.db import models


class User(models.Model):
    email = models.CharField(max_length=110)


class UserRequest(models.Model):
    lon = models.FloatField()
    lat = models.FloatField()
    message = models.CharField(max_length=500)
    expires = models.DateTimeField()
    user = models.ForeignKey(User)

from django.db import models


class User(models.Model):
    email = models.CharField(max_length=110)
    tokens = models.IntegerField(default=0)


class UserRequest(models.Model):
    lon = models.FloatField()
    lat = models.FloatField()
    message = models.CharField(max_length=500)
    expires = models.DateTimeField()
    user = models.ForeignKey(User, related_name='user_requests')
    bounty = models.IntegerField(default=0)


class UserResponse(models.Model):
    text = models.CharField(max_length=500)
    votes = models.IntegerField(blank=True, null=True)
    user_request = models.ForeignKey(UserRequest,
                                     related_name='responses')
    user = models.ForeignKey(User, related_name='user_responses')

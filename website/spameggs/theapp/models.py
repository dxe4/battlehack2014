from django.db import models

from theapp.util import lat_long_distance


class LocationManager(models.Manager):

    def find_closest(self, city, lon, lat, max_distance=5):
        '''
        Not scalable probably, for now its ok
        '''
        requests = UserRequest.objects.filter(city=city)

        result = []
        for i in requests:
            distance = lat_long_distance(lon, lat, i.lon, i.lat)
            if distance <= max_distance:
                result.append(distance, i)

        return result


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

    country = models.CharField(max_length=150)
    city = models.CharField(max_length=150)
    location = models.CharField(max_length=250)
    country_code = models.CharField(max_length=3)

    objects = LocationManager()


class UserResponse(models.Model):
    text = models.CharField(max_length=500)
    votes = models.IntegerField(blank=True, null=True)
    user_request = models.ForeignKey(UserRequest,
                                     related_name='responses')
    user = models.ForeignKey(User, related_name='user_responses')
    accepted = models.BooleanField(default=False)

from uuid import uuid4


class UserRequest(object):

    def __init__(self, lon, lat, message, expires, from_user):
        self.lon = lon
        self.lat = lat
        self.message = message
        self.expires = expires
        self.from_user = from_user
        self.uid = str(uuid4()).split('-')[0]

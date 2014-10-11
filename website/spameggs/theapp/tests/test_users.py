from django.test import TestCase, Client
from theapp.models import User

from django.contrib.auth.hashers import make_password


class TestUsers(TestCase):

    def setUp(self):
        password = 'spam'
        self.user = User.objects.create_user(
            'spam@eggs.coffee',
            email='spam@eggs.coffee', password=password)
        self.user.is_active = True
        self.user.save()

    def test_login(self):
        client = Client()
        data = {'username': 'spam@eggs.coffee', 'password': 'spam'}
        response = client.post('/login', data=data)

        assert response.status_code == 200

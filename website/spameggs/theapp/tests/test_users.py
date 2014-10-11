from django.test import TestCase, Client
from theapp.models import User

from django.contrib.auth.hashers import make_password


class TestUsers(TestCase):

    def setUp(self):
        password = 'spam'
        self.user = User.objects.create_user(
            'spam@eggs.coffee',
            username='spam@eggs.coffee', password=password,
            is_active=True)
        self.user.save()

    def test_login(self):
        client = Client()
        response = client.post('/login', username='spam@eggs.coffee',
                               password='spam')

        assert response.status_code == 200
        self.assertIn('_auth_user_id', self.client.session)

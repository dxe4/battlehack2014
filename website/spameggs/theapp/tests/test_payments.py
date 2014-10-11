from braintree.test.nonces import Nonces
from django.test import TestCase, Client
from theapp.models import User

from ..payments import TokenPurchase


class TokenPurchaseTestCase(TestCase):

    def setUp(self):
        self.client = Client()
        password = 'spam'
        self.user = User.objects.create_user(
            'spam@eggs.coffee',
            email='spam@eggs.coffee', password=password)
        self.user.is_active = True
        self.user.save()

    def _login(self):
        data = {'username': 'spam@eggs.coffee', 'password': 'spam'}
        self.client.post('/login', data)

    def test_purchase_100(self):
        self._login()
        data = {
            'from_user': 'spam@eggs.coffee',
            'nonce': Nonces.Transactable,
            'amount': 100
        }
        response = self.client.post('/purchase_tokens', data)

        assert response.status_code == 200

        user = User.objects.get(email='spam@eggs.coffee')
        assert user.tokens == 100

    def test_get_client_token(self):
        self._login()
        response = self.client.post('/purchase_tokens', {
            'from_user': 'spam@eggs.coffee'
        })

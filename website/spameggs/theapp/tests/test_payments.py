from braintree.test.nonces import Nonces
from django.test import TestCase, Client
from theapp.models import User

from ..payments import TokenPurchase


class TokenPurchaseTestCase(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create(email="me@swistofon.pl")

    def test_purchase_100(self):
        data = {
            'from_user': 'me@swistofon.pl',
            'nonce': Nonces.Transactable,
            'amount': 100
        }
        response = self.client.post('/purchase_tokens', data)

        assert response.status_code == 200

        user = User.objects.get(email='me@swistofon.pl')
        assert user.tokens == 100


    def test_get_client_token(self):
        response = self.client.post('/purchase_tokens', {
            'from_user': 'me@swistofon.pl'
        })


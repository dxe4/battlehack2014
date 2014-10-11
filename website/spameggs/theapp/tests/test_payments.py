from braintree.test.nonces import Nonces
from django.test import TestCase, Client
from theapp.models import User

from ..payments import TokenPurchase

class TokenPurchaseTestCase(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create(email="me@swistofon.pl")


    def test_purchase_100(self):
        response = self.client.post('/purchase_tokens', {
                'from_user': 'me@swistofon.pl',
                'nonce': Nonces.Transactable,
                'amount': 100
            })

        

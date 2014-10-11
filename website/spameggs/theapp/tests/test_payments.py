from braintree.test.nonces import Nonces
from django.test import TestCase, Client
from theapp.models import User

from ..payments import TokenPurchase

class AnimalTestCase(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User(email="me@swistofon.pl")


    def test_purchase_100(self):
        self.client.post('purchase_tokens', {
        	'from_user': 'me@swistofon.pl',
        	'nonce': Nonces.Transactable,
        	'amount': 100
        	})

        assert self.user.tokens == 100
        

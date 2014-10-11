import braintree

class RequestToken(object):
	"""docstring for RequestToken"""
	def __init__(self, arg):
		super(RequestToken, self).__init__()
		self.arg = arg


	def buy(nonce, user):
		result = braintree.Transaction.sale({
		    "amount": "100.00",
		    "payment_method_nonce": nonce,
		})

		if result.is_success:
			user.tokens += 100;
			user.save()
    		return True
    	else:
    		return result.errors.deep_errors




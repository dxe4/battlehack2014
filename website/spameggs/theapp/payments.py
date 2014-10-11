import braintree

braintree.Configuration.configure(braintree.Environment.Sandbox,
								  merchant_id="7kf5yx5drbwk7zt5",
								  public_key="kk4d5dczg48qhqb3",
								  private_key="56e20a585ec017d5bcb102dee39cb921")

class TokenPurchase(object):
	"""docstring for TokenPurchase"""
	def __init__(self, arg):
		super(TokenPurchase, self).__init__()
		self.arg = arg

	@classmethod
	def generate_client_token(user):
		client_token = braintree.ClientToken.generate({
			"customer_id": user.id
		})

		return client_token

	@classmethod
	def buy(nonce, user, amount):
		result = braintree.Transaction.sale({
			"amount": "{}.00".format(amount/100),
			"payment_method_nonce": nonce,
		})

		if result.is_success:
			user.tokens += 100
			user.save()
			return True
		else:
			return result.errors.deep_errors




# views, move them later




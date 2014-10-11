from django.conf.urls import patterns, url
from theapp.views import (CreateRequest, CreateResponse, 
	ListResponses, AcceptAnswer, PurchaseTokens) 

urlpatterns = patterns(
    '',
    url(r'^create_request$', CreateRequest.as_view(), name='create_request'),
    url(r'^create_response$', CreateResponse.as_view(), name='create_response'),
    url(r'^list_responses$', ListResponses.as_view(), name='list_responses'),
    url(r'^accept_answer$', AcceptAnswer.as_view(), name='accept_answer'),
    url(r'^purchase_tokens$', PurchaseTokens.as_view(), name='purchase_tokens')
)

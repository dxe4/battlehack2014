from django.conf.urls import patterns, url
from theapp.views import CreateRequest

urlpatterns = patterns(
    '',
    url(r'^create_request$', CreateRequest.as_view(), name='create_request'),
)

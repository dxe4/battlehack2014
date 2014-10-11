from django.conf.urls import patterns, url
from theapp.views import index

urlpatterns = patterns(
    '',
    url(r'^$', index, name='index'),
)

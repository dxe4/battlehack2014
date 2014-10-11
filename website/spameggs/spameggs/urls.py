from django.conf.urls import patterns, include, url
from theapp import urls as theapp_urls

urlpatterns = patterns(
    '',
    # Examples:
    # url(r'^$', 'spameggs.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # url(r'^admin/', include(admin.site.urls)),
    (r'', include(theapp_urls, namespace='eggs', app_name='eggs')),
)

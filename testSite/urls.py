from django.conf.urls import patterns, url


urlpatterns = patterns('testSite.views',
                       url(r'^(?:(?P<id>\d+)/)?$', 'index'),
                       url(r'^good/(?P<id>\d+)/$', 'good'))

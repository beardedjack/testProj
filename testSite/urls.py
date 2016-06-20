from django.conf.urls import patterns, url
from testSite import views

urlpatterns = patterns('',
                       url(r'^(?:(?P<id>\d+)/)?$', views.index, name="index"),
                       url(r'^good/(?P<id>\d+)/$', views.good, name="good"))

from django.conf.urls import patterns, url
from testSite import views
from testSite.twviews import GoodListView, GoodDetailView

# urlpatterns = patterns('',
#                        url(r'^(?:(?P<id>\d+)/)?$', views.index, name="index"),
#                        url(r'^good/(?P<id>\d+)/$', views.good, name="good"))


urlpatterns = patterns('',
                        url(r'^(?:(?P<id>\d+)/)?$', GoodListView.as_view(), name="index"),
                        url(r'^good/(?P<id>\d+)/$', GoodDetailView.as_view(), name="good"))

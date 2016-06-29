from django.conf.urls import patterns, url
from testSite.twviews import GoodListView, GoodDetailView

from testSite.twviews import GoodCreate, GoodUpdate, GoodDelete

urlpatterns = patterns('',
    url(r'^(?:(?P<id>\d+)/)?$', GoodListView.as_view(), name="index"),
    url(r'^good/(?P<id>\d+)/$', GoodDetailView.as_view(), name="good"),
    url(r'^(?P<id>\d+)/add/$', GoodCreate.as_view(), name="good_add"),
    url(r'^good/(?P<id>\d+)/edit/$', GoodUpdate.as_view(), name="good_edit"),
    url(r'^good/(?P<id>\d+)/delete/$', GoodDelete.as_view(), name="good_delete"),
)


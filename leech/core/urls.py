from django.conf.urls import patterns, url

from .views import BlockList, BlockUrl


urlpatterns = patterns(
    '',  # view prefix
    url(r'^$', BlockList.as_view(), name='index'),
    url(r'^block-url/', BlockUrl.as_view(), name='block-url'),
)

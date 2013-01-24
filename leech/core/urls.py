from django.conf.urls import patterns, url

from .views import About, AllTimeStats, BlockList, BlockUrl


urlpatterns = patterns(
    '',  # view prefix
    url(r'^$', BlockList.as_view(), name='index'),
    url(r'^block-url/', BlockUrl.as_view(), name='block-url'),
    url(r'^about/$', About.as_view(), name='about'),
    url(r'^stats/all-time.json', AllTimeStats.as_view(), name='stats-all-time')
)

from django.conf.urls import patterns, url

from .views import BlockList


urlpatterns = patterns(
    '',  # view prefix
    url(r'^$', BlockList.as_view(), name=''),
)

from django.conf.urls import patterns, include, url
from django.contrib import admin


admin.autodiscover()

urlpatterns = patterns(
    '',  # view prefix
    url(r'^browserid/', include('django_browserid.urls')),
    url(r'^admin/', include(admin.site.urls)),
)

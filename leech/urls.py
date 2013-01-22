from django.conf.urls import patterns, include, url
from django.contrib import admin


admin.autodiscover()

urlpatterns = patterns(
    '',  # view prefix
    url(r'^admin/', include(admin.site.urls)),
)

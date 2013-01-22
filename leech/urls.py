from django.conf.urls import patterns, include, url
from django.contrib import admin


admin.autodiscover()

urlpatterns = patterns(
    '',  # view prefix
    url(r'^$', include('leech.core.urls')),
    url(r'^browserid/', include('django_browserid.urls')),
    url(r'^logout/', 'django.contrib.auth.views.logout', name='logout'),
    url(r'^admin/', include(admin.site.urls)),
)

import os

from django.conf.urls.defaults import patterns, include, url
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    (r'^api/', include('api.urls')),    
    (r'^search/', include('haystack.urls')),
    url(r'^', include('mainapp.urls')),
    
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^m/$', 'django.views.static.serve', {
                'path': 'index.html',
                'document_root': settings.MOBILE_ROOT,
    }),
    url(r'^mobile/$', 'django.views.static.serve', {
                'path': 'index.html',
                'document_root': settings.MOBILE_ROOT,
    }),

    url(r'^mobile/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MOBILE_ROOT,
    }),
)


if settings.DEBUG:
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns
    urlpatterns += staticfiles_urlpatterns()

    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),

   )
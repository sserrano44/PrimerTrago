from django.conf.urls.defaults import patterns, include, url


urlpatterns = patterns('',
    url(r'^$', 'mainapp.views.home', name='mainapp_home'),
    url(r'^bar/(?P<id>[\d]+)/$', 'mainapp.views.bar', name='mainapp_bar'),
    url(r'^bar/(?P<slug>[\w\d_-]+)/$', 'mainapp.views.bar', name='mainapp_bar'),
)

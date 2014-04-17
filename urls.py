from django.conf.urls import patterns, url, include
from settings import STATIC_ROOT, MEDIA_ROOT

from django.contrib import admin
admin.autodiscover()


handler500 = 'djangotoolbox.errorviews.server_error'
handler404 = 'hackaglobal.views.handler404'

urlpatterns = patterns('',

    #My Apps
    url(r'^api/', include('apihg.urls')),
    url(r'accounts/', include('accounts.urls')),
    url(r'hackacity/', include('hackacities.urls')),
    url(r'', include('hackaglobal.urls')),


    #External Apps
    url(r'', include('social_auth.urls')),


    #Admin
    ('^admin/', include(admin.site.urls)),


    #Static files
    (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': STATIC_ROOT}),
    (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': MEDIA_ROOT}),

)
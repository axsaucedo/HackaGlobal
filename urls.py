from django.conf.urls import patterns, url, include
from settings import STATIC_ROOT

from django.contrib import admin
admin.autodiscover()

handler500 = 'djangotoolbox.errorviews.server_error'
handler404 = 'hackaglobal.views.handler404'

urlpatterns = patterns('',

    #Login and API
    url(r'^api/', include('apihg.urls')),
    url(r'', include('social_auth.urls')),
    url(r'', include('accounts.urls')),
    url(r'', include('hackaglobal.urls')),


    #Admin
    ('^admin/', include(admin.site.urls)),


    #Static files
    (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': STATIC_ROOT}),

)
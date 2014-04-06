from django.conf.urls.defaults import *
from hackaglobal import views, ajax
from django.contrib import admin
from django.conf.urls import patterns
from apihg import urls as apihgurls

from models import Event

handler500 = 'djangotoolbox.errorviews.server_error'

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

handler404 = 'hackaglobal.views.handler404'

urlpatterns = patterns('',

    url(r'^api/', include(apihgurls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    url(r'^$', views.home, name='home'),

    #FrontEnd
    url(r'^web/(?P<country>\w+)/$', views.getCountryListView, name='country_list_view'),

    url(r'^find/$', views.find_events, name='find_events'),
    url(r'^create/$', views.add_event, name='add_event'),
    url(r'^manage/$', views.manage_events, name='manage_events'),
    url(r'^delete/(?P<event_id>.+)/$', views.delete_event, name='delete_event'),
    url(r'^manage/(?P<event_id>.+)/$', views.edit_event, name='edit_event'),
    url(r'^event/(?P<event_id>.+)/$', views.view_event, name='manage_events'),

    # Handling all AJAX calls
    url(r'^attend_event/$', ajax.attend_event, name='attend_event'),
    url(r'^add_staff/$', ajax.add_staff, name='add_staff'),
    url(r'^remove_staff/$', ajax.remove_staff, name='remove_staff'),

    # Account authentication
    (r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}),
    (r'^logout/$', 'django.contrib.auth.views.logout', {'next_page' : '/'}),
    url(r'^signup/$', views.apply),

    # Account management
    url(r'^accounts/edit/password/$', views.edit_password, name='edit_password'),
    url(r'^accounts/edit/$', views.edit_account, name='edit_account'),
    url(r'^accounts/view/(?P<username>.+)/$', views.view_account, name='view_account'),


    ('^admin/', include(admin.site.urls)),
)

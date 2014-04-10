from django.conf.urls import patterns, url, include
from hackaglobal import views, ajax

urlpatterns = patterns('',

    #FrontEnd
    url(r'^$', views.home, name='home'),
    url(r'^web/(?P<country>.+)/$', views.getCountryListView, name='country_list_view'),


    #Backend
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
)

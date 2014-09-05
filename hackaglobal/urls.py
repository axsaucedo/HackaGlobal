from django.conf.urls import patterns, url, include
from hackaglobal import views, ajax

urlpatterns = patterns('',

    #FrontEnd
    url(r'^$', views.home, name='home'),
    url(r'^web/(?P<country>.+)/$', views.getCountryListView, name='country_list_view'),


    #Backend
    url(r'^find/$', views.find_events, name='find_events'),
    url(r'^create/$', views.add_event, name='add_event'),
    url(r'^manage/$', views.manage_events, name='manage_all'),
    url(r'^delete/(?P<event_id>.+)/$', views.delete_event, name='delete_event'),
    url(r'^manage/(?P<event_id>.+)/$', views.edit_event, name='edit_event'),
    url(r'^event/(?P<event_id>.+)/$', views.view_event, name='manage_event'),


    # Handling all AJAX calls
    url(r'^attend_event/$', ajax.attend_event, name='attend_event'),
    url(r'^add_container/$', ajax.add_container, name='add_container'),
    url(r'^remove_container/$', ajax.remove_container, name='remove_container'),
    url(r'^add_team/$', ajax.add_team, name='add_team'),
    url(r'^remove_team/$', ajax.remove_team, name='remove_team'),
)

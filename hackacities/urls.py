from django.conf.urls import patterns, url, include
from hackacities import views

urlpatterns = patterns('',

    # Hackacity management
    url(r'^view/(?P<hc>\w+)/$', views.view_hackacity, name='view_hackacity'),

    # Hackacity management
    url(r'^edit/(?P<hc>\w+)/$', views.edit_hackacity, name='edit_hackacity'),
)

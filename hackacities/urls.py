from django.conf.urls import patterns, url, include
from hackacities import views

urlpatterns = patterns('',

    # Hackacity management
    url(r'^view/(?P<hc>.+)/$', views.view_hackacity, name='view_hackacity'),

    # Hackacity management
    url(r'^edit/(?P<hc>.+)/$', views.edit_hackacity, name='edit_hackacity'),
)

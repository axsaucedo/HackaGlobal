from django.conf.urls import patterns, url, include
from hackacities import views

urlpatterns = patterns('',

    # Hackacity management
    url(r'^view/(?P<hc>\w+)/$', views.view_hackacity, name='hackacity'),
)

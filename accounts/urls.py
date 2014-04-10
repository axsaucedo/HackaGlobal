from django.conf.urls import patterns, url, include
import views

urlpatterns = patterns('',

    # Account authentication
    (r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}),
    (r'^logout/$', 'django.contrib.auth.views.logout', {'next_page' : '/'}),
    url(r'^signup/$', views.apply),

    # Account management
    url(r'^accounts/edit/password/$', views.edit_password, name='edit_password'),
    url(r'^accounts/edit/$', views.edit_account, name='edit_account'),
    url(r'^accounts/view/(?P<username>.+)/$', views.view_account, name='view_account'),
)
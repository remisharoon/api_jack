from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from . import views
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'api_jack.views.home', name='home'),
    # url(r'^api_jack/', include('api_jack.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^users/?$', views.UserList.as_view()),
    url(r'^files/?$', views.FilesList.as_view()), 
    url(r'^sys_status/?$', views.SystemStatus.as_view()),              
)

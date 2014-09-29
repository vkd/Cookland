from django.conf.urls import patterns, include, url

from django.contrib import admin
from house_apps.views import home as house_apps_index
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'house_apps.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^cook/', include('cookland.urls', namespace='cook')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^bugs/', include('bugtracker.urls', namespace='bugs')),
)

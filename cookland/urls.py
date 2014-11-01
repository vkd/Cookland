from django.conf.urls import patterns, include, url

from django.contrib import admin
from cookland.views import home as cookland_index
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'cookland.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^cook/', include('cook.urls', namespace='cook')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^bugs/', include('bugtracker.urls', namespace='bugs')),
)

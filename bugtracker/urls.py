from django.conf.urls import patterns, include, url
from bugtracker.views import *

urlpatterns = patterns('',
	url(r'^$', index),
)
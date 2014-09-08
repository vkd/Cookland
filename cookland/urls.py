from django.conf.urls import *
from cookland.views import index

urlpatterns = patterns('',
	url(r'^$', index),
)
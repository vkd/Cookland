from django.conf.urls import *
from cookland.views import index as cook_index

urlpatterns = patterns('',
	url(r'^$', cook_index),
)
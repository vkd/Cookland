from django.conf.urls import *
from cookland.views import index as cook_index
from cookland.views import form_input

urlpatterns = patterns('',
	url(r'^admin/', form_input),
	url(r'^$', cook_index),
)
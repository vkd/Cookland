from django.conf.urls import *

from cookland.views import *

urlpatterns = patterns('',
	url(r'^admin/', form_input),
	url(r'^recipes/', recipes_list),
	url(r'^404/', custom_not_found_page),
	url(r'^$', index),
)
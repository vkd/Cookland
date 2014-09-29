from django.conf.urls import *

from cookland.views import *

urlpatterns = patterns('',
	url(r'^test/', test_page, name='test'),
	url(r'^admin/', form_input, name='admin'),
	url(r'^recipes/', recipes_list, name='recipes'),
	url(r'^404/', custom_not_found_page, name='404'),
	url(r'^$', index, name='index'),
)
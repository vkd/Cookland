from django.conf.urls import *
from django.core.urlresolvers import reverse_lazy

from cook.views import *

urlpatterns = patterns(
    '',
    url(r'^recipe/(?P<pk>[0-9]+)/', view_recipe, name='view_recipe'),
    url(r'^recipe/add/', add_recipe, name='add_recipe'),
    url(r'^recipe/delete/(?P<pk>[0-9]+)/', delete_recipe, name='delete_recipe'),
    url(r'^recipe/edit/(?P<pk>[0-9]+)/', edit_recipe, name='edit_recipe'),
    url(r'^recipes/', recipes, name='recipes'),
    url(r'^404/', custom_not_found_page, name='404'),
    url(r'^login/', login_action, name="login"),
    url(r'^logout/$', 'django.contrib.auth.views.logout',
        {"next_page": reverse_lazy('cook:index')}, name="logout"),
    url(r'^$', index, name='index'),
)

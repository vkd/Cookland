from django.shortcuts import render

# Create your views here.
from django.template import loader, Context
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth import authenticate, login

from cook.models import *
from cook.forms import *

def test_page(request):
	context = { }
	return render(request, 'cook/test.html', context)

def add_recipe_page(request):
	context = { }
	return render(request, 'cook/add_recipe.html', context)

def add_new_recipe(request):
	# if this is a POST request we need to process the form data
	if request.method == 'POST':
		# create a form instance and populate it with data from the request:
		form = AddRecipeForm(request.POST)
		# check whether it's valid:
		if form.is_valid():
			# process the data in form.cleaned_data as required
			# ...
			r = Recipe(name=form.cleaned_data['recipe_name'])
			r.save()
			# redirect to a new URL:
			return HttpResponseRedirect(reverse_lazy('cook:recipes'))
			# return HttpResponseRedirect('/thanks/?text=%s' % form.cleaned_data['recipe_name'])

	# if a GET (or any other method) we'll create a blank form
	# else:
	# 	form = NameForm()

	return HttpResponseRedirect(reverse_lazy('cook:add_recipe'))

def review_recipes_page(request):
	context = { }
	return render(request, 'cook/review_recipes.html', context)

def recipes_list_page(request):
	context = { }
	return render(request, 'cook/recipes_list.html', context)

def index(request):
	#try:
	#	posts = CookPost.objects.all()
	#except CookPost.DoesNotExist:
	#	raise Http404

	context = { }
	return render(request, 'cook/index.html', context)

def form_input(request):
	context = { }
	return render(request, 'cook/form_input.html', context)

def custom_not_found_page(request):
	context = { }
	return render(request, 'cook/404.html', context)

def recipes_list(request):
	context = { 'recipes' : Recipe.objects.all() }
	return render(request, 'cook/recipes.html', context)
	
def login_action(request):
	username = request.POST['login']
	password = request.POST['password']
	user = authenticate(username=username, password=password)
	if user is not None:
		if user.is_active:
			login(request, user)
			# Redirect to a success page.
		else:
			pass
			# Return a 'disabled account' error message
	else:
		pass
		# Return an 'invalid login' error message.
	return HttpResponseRedirect(reverse_lazy('cook:index'))

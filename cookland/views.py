from django.shortcuts import render

# Create your views here.
from django.template import loader, Context
from django.http import HttpResponse, Http404

from cookland.models import *

def test_page(request):
	context = { }
	return render(request, 'cook/test.html', context)

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
	
	
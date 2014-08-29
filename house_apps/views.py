from django.shortcuts import render

# Create your views here.
from django.template import loader, Context
from django.http import HttpResponse

def home(request):
	t = loader.get_template("home.html")
	c = Context()
	return HttpResponse(t.render(c))
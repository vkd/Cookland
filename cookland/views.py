from django.shortcuts import render

# Create your views here.
from django.template import loader, Context
from django.http import HttpResponse
from cookland.models import CookPost

def index(request):
	posts = CookPost.objects.all()
	t = loader.get_template("index.html")
	c = Context({ 'posts': posts })
	return HttpResponse(t.render(c))
	
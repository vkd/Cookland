from django.shortcuts import render

# Create your views here.
from django.template import loader, Context
from django.http import HttpResponse, Http404

from cookland.models import CookPost

def index(request):
	try:
		posts = CookPost.objects.all()
	except CookPost.DoesNotExist:
		raise Http404

	context = { 'posts': posts }
	return render(request, 'index.html', context)
	
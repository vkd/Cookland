from django.shortcuts import render

# Create your views here.
def index(request):
	context = { }
	return render(request, 'list_bug.html', context)

def revert_to_index():
	pass

from django.views.generic import ListView
from .models import Ticket

class BugListView(ListView):
    model = Ticket
    template_name = 'list_bug.html'

from django.views.generic import DetailView

class BugDetailView(DetailView):
    model = Ticket
    template_name = 'detail_bug.html'

from django.views.generic import CreateView
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.forms import UserCreationForm

class RegisterView(CreateView):
    form_class = UserCreationForm
    template_name = 'register_bug.html'
    success_url = reverse_lazy('index')
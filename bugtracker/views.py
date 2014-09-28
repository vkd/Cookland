from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy

# Create your views here.
def index(request):
	context = { }
	return render(request, 'bugs/list_bug.html', context)

def revert_to_index():
	pass

from django.views.generic import ListView
from .models import Ticket

class BugListView(ListView):
    model = Ticket
    template_name = 'bugs/list_bug.html'

from django.views.generic import DetailView

class BugDetailView(DetailView):
    model = Ticket
    template_name = 'bugs/detail_bug.html'

from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm

class RegisterView(CreateView):
    form_class = UserCreationForm
    template_name = 'bugs/register_bug.html'
    success_url = reverse_lazy('bugs:index')

class BugCreateView(CreateView):
    model = Ticket
    template_name = 'bugs/add_bug.html'
    fields = ['title', 'text']
    success_url = reverse_lazy('bugs:index')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(BugCreateView, self).form_valid(form)

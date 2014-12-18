from django.shortcuts import render

# Create your views here.
from django.template import loader, Context
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth import authenticate, login

from cook.models import *
from cook.forms import *


def add_recipe(request):
    if request.user.is_authenticated():
        if request.method == 'POST':
            form = AddRecipeForm(request.POST)
            if form.is_valid():
                r = Recipe(
                    name=form.cleaned_data['recipe_name'],
                    discribe=form.cleaned_data['discribe']
                )
                r.save()

                return HttpResponseRedirect(reverse_lazy('cook:recipes'))
        else:
            context = {}
            return render(request, 'cook/add_recipe.html', context)
    else:
        return HttpResponseRedirect(reverse_lazy('cook:index'))


def view_recipe(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    context = {'recipe': recipe}
    return render(request, 'cook/view_recipe.html', context)


def delete_recipe(request, pk):
    if request.user.is_authenticated():
        recipe = Recipe.objects.get(pk=pk)
        recipe.delete()
        return HttpResponseRedirect(reverse_lazy('cook:recipes'))
    else:
        return HttpResponseRedirect(reverse_lazy('cook:index'))


def edit_recipe(request, pk):
    if request.user.is_authenticated():
        # recipe = Recipe.objects.get(pk=pk)
        # form = AddRecipeForm(instance=recipe)
        context = {}
        # context = { 'from': form }
        return render(request, 'cook/add_recipe.html', context)
        # return HttpResponseRedirect(reverse_lazy('cook:recipes'))
    else:
        return HttpResponseRedirect(reverse_lazy('cook:index'))


def index(request):
    # try:
    #   posts = CookPost.objects.all()
    # except CookPost.DoesNotExist:
    #   raise Http404

    context = {}
    return render(request, 'cook/index.html', context)


def custom_not_found_page(request):
    context = {}
    return render(request, 'cook/404.html', context)


def recipes(request):
    context = {'recipes': Recipe.objects.all()}
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

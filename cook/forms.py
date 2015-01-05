from django import forms

from cook.models import Recipe

class AddRecipeForm(forms.Form):
	recipe_name = forms.CharField(max_length=150)

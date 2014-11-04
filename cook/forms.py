from django import forms

from cook.models import Recipe

class AddRecipeForm(forms.ModelForm):
    recipe_name = forms.CharField(label='name')
    class Meta:
        model=Recipe

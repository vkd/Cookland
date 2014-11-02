from django import forms

class AddRecipeForm(forms.Form):
    recipe_name = forms.CharField(label='name')

from django import forms

from cook.models import Recipe


class AddRecipeForm(forms.ModelForm):
    # recipe_name = forms.CharField(max_length=150)
    # discribe = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = Recipe
        fields = ('name', 'discribe', 'image', )

from django.contrib import admin
from cook.models import *

class TagAdmin(admin.ModelAdmin):
	list_display = ('name', )

class ProduceAdmin(admin.ModelAdmin):
	list_display = ('name', )

class RecipeAdmin(admin.ModelAdmin):
	list_display = ('name', )

class IngredientAdmin(admin.ModelAdmin):
	list_display = ('value', 'produce', 'recipe', )

class Recipe_TagsAdmin(admin.ModelAdmin):
	pass;

# Register your models here.
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Produce, ProduceAdmin)
admin.site.register(Recipe_Tags, Recipe_TagsAdmin)

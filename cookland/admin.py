from django.contrib import admin
from cookland.models import Recipe, Tag, Ingredient, Produce

class TagAdmin(admin.ModelAdmin):
	list_display = ('name', )

class ProduceAdmin(admin.ModelAdmin):
	list_display = ('name', )

class RecipeAdmin(admin.ModelAdmin):
	list_display = ('name', )

class IngredientAdmin(admin.ModelAdmin):
	list_display = ('value', 'produce', 'recipe', )

# Register your models here.
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Produce, ProduceAdmin)

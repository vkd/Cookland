from django.contrib import admin
from cookland.models import CookPost, Recipe, Tag, Ingredient, Produce

class TagAdmin(admin.ModelAdmin):
	list_display = ('name', )

class CookPostAdmin(admin.ModelAdmin):
	list_display = ('title',)

class RecipeAdmin(admin.ModelAdmin):
	list_display = ('name',)

class IngredientAdmin(admin.ModelAdmin):
	list_display = ('value', )

class ProduceAdmin(admin.ModelAdmin):
	list_display = ('name', )

# Register your models here.
admin.site.register(CookPost, CookPostAdmin)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Produce, ProduceAdmin)

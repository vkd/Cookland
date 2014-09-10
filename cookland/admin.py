from django.contrib import admin
from cookland.models import CookPost

class CookPostAdmin(admin.ModelAdmin):
	list_display = ('title',)

# Register your models here.
admin.site.register(CookPost, CookPostAdmin)

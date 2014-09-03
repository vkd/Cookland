from django.contrib import admin
from cookland.models import CookPost, CookPostAdmin

# Register your models here.
admin.site.register(CookPost, CookPostAdmin)

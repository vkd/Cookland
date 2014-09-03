from django.db import models
from django.contrib import admin

# Create your models here.
class CookPost(models.Model):
	title = models.CharField(max_length=150)
	body = models.TextField()

	#class Meta:
	#	ordering = ('-timestamp',)

class CookPostAdmin(admin.ModelAdmin):
	list_display = ('title',)


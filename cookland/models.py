from django.db import models
from django.contrib import admin

class Ingredient(models.Model):
	name = models.CharField(max_length=150)

# Create your models here.
class CookPost(models.Model):
	title = models.CharField(max_length=150)
	body = models.TextField()

	#class Meta:
	#	ordering = ('-timestamp',)



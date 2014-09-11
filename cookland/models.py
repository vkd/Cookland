from django.db import models
from django.contrib import admin

class Produce(models.Model):
	name = models.CharField(max_length=150)

class Recipe(models.Model):
	name = models.CharField(max_length=150)
	ingredients = models.ManyToManyField(Produce, related_name='recipes', through='Ingredient')
	discribe = models.TextField()
	image = models.ImageField()

class Ingredient(models.Model):
	value = models.CharField(max_length=150)
	produce = models.ForeignKey(Produce)
	recipe = models.ForeignKey(Recipe)

# Create your models here.
class CookPost(models.Model):
	title = models.CharField(max_length=150)
	body = models.TextField()

	#class Meta:
	#	ordering = ('-timestamp',)



from django.db import models
from django.contrib import admin

class Tag(models.Model):
	name = models.CharField(max_length=150)

	def __unicode__(self):
		return name

class Produce(models.Model):
	name = models.CharField(max_length=150)

	def __unicode__(self):
		return name

class Recipe(models.Model):
	name = models.CharField(max_length=150)
	ingredients = models.ManyToManyField(Produce, related_name='recipes', through='Ingredient')
	discribe = models.TextField()
	image = models.ImageField(blank=True)
	tags = models.ManyToManyField(Tag, related_name='recipes', through='Recipe_Tags')

	def __unicode__(self):
		return name

class Recipe_Tags(models.Model):
	recipe = models.ForeignKey(Recipe)
	tag = models.ForeignKey(Tag)

class Ingredient(models.Model):
	value = models.CharField(max_length=150)
	produce = models.ForeignKey(Produce)
	recipe = models.ForeignKey(Recipe)

	#def __unicode__(self):
	#	return "{} кг {}".format(value, produce.name)

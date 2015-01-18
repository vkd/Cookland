from django.db import models
from uuid import uuid4


def rename_image_to_pk(instance, filename):
    return "recipe_images/%s.%s" % (uuid4().hex, filename.split('.')[-1])


class Tag(models.Model):
    name = models.CharField(max_length=150)


class Produce(models.Model):
    name = models.CharField(max_length=150)


class Recipe(models.Model):
    name = models.CharField(max_length=150)
    ingredients = models.ManyToManyField(Produce, related_name='recipes', through='Ingredient')
    discribe = models.TextField()
    image = models.ImageField(blank=True, null=True, upload_to=rename_image_to_pk)
    tags = models.ManyToManyField(Tag, related_name='recipes', through='Recipe_Tags')
    date_create = models.DateTimeField(auto_now_add=True, editable=False)

    class Meta():
        ordering = ('-date_create',)


class Recipe_Tags(models.Model):
    recipe = models.ForeignKey(Recipe)
    tag = models.ForeignKey(Tag)


class Ingredient(models.Model):
    value = models.CharField(max_length=150)
    produce = models.ForeignKey(Produce)
    recipe = models.ForeignKey(Recipe)


# Receive the pre_delete signal and delete the file associated with the model instance.
from django.db.models.signals import pre_delete
from django.dispatch.dispatcher import receiver


@receiver(pre_delete, sender=Recipe)
def mymodel_delete(sender, instance, **kwargs):
    # Pass false so FileField doesn't save the model.
    instance.image.delete(False)

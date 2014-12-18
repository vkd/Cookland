# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


def fill_date_create(apps, schema_editor):
    Recipe = apps.get_model("cook", "Recipe")
    for recipe in Recipe.objects.all():
        recipe.date_create = datetime.datetime.now()
        recipe.save()


class Migration(migrations.Migration):

    dependencies = [
        ('cook', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='date_create',
            field=models.DateTimeField(null=True, auto_now_add=True),
            preserve_default=True,
        ),
        migrations.RunPython(fill_date_create),
        migrations.AlterField(
            model_name='recipe',
            name='date_create',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]

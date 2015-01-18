# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import cook.models


class Migration(migrations.Migration):

    dependencies = [
        ('cook', '0004_recipe_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='image',
            field=models.ImageField(blank=True, upload_to=cook.models.rename_image_to_pk, null=True),
        ),
    ]

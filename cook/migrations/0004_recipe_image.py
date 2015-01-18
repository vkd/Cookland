# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cook', '0003_auto_20150118_1430'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='image',
            field=models.ImageField(upload_to='recipe_images', null=True, blank=True),
            preserve_default=True,
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('youthPlatform', '0004_idea_jobad_trainingad'),
    ]

    operations = [
        migrations.AddField(
            model_name='idea',
            name='tags',
            field=models.CharField(default='', max_length=150),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='idea',
            name='title',
            field=models.CharField(default='title', max_length=150),
            preserve_default=True,
        ),
    ]

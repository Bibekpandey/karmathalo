# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('youthPlatform', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='accountType',
            field=models.IntegerField(default=1),
            preserve_default=True,
        ),
    ]

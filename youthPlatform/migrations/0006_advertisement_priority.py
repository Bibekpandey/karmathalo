# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('youthPlatform', '0005_auto_20150218_2003'),
    ]

    operations = [
        migrations.AddField(
            model_name='advertisement',
            name='priority',
            field=models.IntegerField(default=3),
            preserve_default=True,
        ),
    ]

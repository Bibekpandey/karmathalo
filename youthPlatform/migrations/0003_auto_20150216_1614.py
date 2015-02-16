# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('youthPlatform', '0002_auto_20150216_1608'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advertisement',
            name='endDate',
            field=models.DateField(),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='advertisement',
            name='startDate',
            field=models.DateField(default=datetime.date.today),
            preserve_default=True,
        ),
    ]

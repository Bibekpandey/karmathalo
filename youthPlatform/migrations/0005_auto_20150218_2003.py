# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('youthPlatform', '0004_auto_20150218_2002'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='advertisement',
            name='endDate',
        ),
        migrations.RemoveField(
            model_name='advertisement',
            name='priority',
        ),
        migrations.RemoveField(
            model_name='advertisement',
            name='startDate',
        ),
    ]

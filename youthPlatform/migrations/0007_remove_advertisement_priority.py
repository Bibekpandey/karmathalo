# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('youthPlatform', '0006_advertisement_priority'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='advertisement',
            name='priority',
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('youthPlatform', '0002_auto_20150218_0445'),
    ]

    operations = [
        migrations.RenameField(
            model_name='advertisement',
            old_name='detail',
            new_name='description',
        ),
    ]

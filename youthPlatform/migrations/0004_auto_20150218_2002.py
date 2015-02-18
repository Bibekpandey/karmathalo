# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('youthPlatform', '0003_idea_account'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='advertisement',
            name='institutionContact',
        ),
        migrations.RemoveField(
            model_name='advertisement',
            name='institutionDistrict',
        ),
        migrations.RemoveField(
            model_name='advertisement',
            name='institutionEmail',
        ),
        migrations.RemoveField(
            model_name='advertisement',
            name='institutionLocation',
        ),
        migrations.RemoveField(
            model_name='advertisement',
            name='institutionWebsite',
        ),
        migrations.RemoveField(
            model_name='advertisement',
            name='qualification',
        ),
        migrations.DeleteModel(
            name='Qualification',
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('youthPlatform', '0002_remove_idea_account'),
    ]

    operations = [
        migrations.AddField(
            model_name='idea',
            name='account',
            field=models.ForeignKey(default=1, to='youthPlatform.Account'),
            preserve_default=False,
        ),
    ]

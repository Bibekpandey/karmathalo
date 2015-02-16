# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('firstname', models.CharField(max_length=30)),
                ('lastname', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=50)),
                ('contact', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=40)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Account',
            fields=[
                ('person_ptr', models.OneToOneField(serialize=False, auto_created=True, to='youthPlatform.Person', parent_link=True, primary_key=True)),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('accountType', models.CharField(max_length=30)),
                ('institution', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=('youthPlatform.person',),
        ),
    ]

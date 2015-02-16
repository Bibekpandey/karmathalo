# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('youthPlatform', '0003_auto_20150216_1614'),
    ]

    operations = [
        migrations.CreateModel(
            name='Idea',
            fields=[
                ('person_ptr', models.OneToOneField(serialize=False, auto_created=True, primary_key=True, parent_link=True, to='youthPlatform.Person')),
                ('isAnonymous', models.BooleanField(default=False)),
                ('description', models.TextField()),
            ],
            options={
            },
            bases=('youthPlatform.person',),
        ),
        migrations.CreateModel(
            name='JobAd',
            fields=[
                ('advertisement_ptr', models.OneToOneField(serialize=False, auto_created=True, primary_key=True, parent_link=True, to='youthPlatform.Advertisement')),
                ('skill', models.CharField(max_length=100)),
                ('salary', models.IntegerField()),
                ('post', models.CharField(max_length=50)),
                ('givesTraining', models.BooleanField(default=False)),
            ],
            options={
            },
            bases=('youthPlatform.advertisement',),
        ),
        migrations.CreateModel(
            name='TrainingAd',
            fields=[
                ('advertisement_ptr', models.OneToOneField(serialize=False, auto_created=True, primary_key=True, parent_link=True, to='youthPlatform.Advertisement')),
                ('duration', models.CharField(max_length=40)),
                ('cost', models.IntegerField()),
                ('givesJob', models.BooleanField(default=False)),
            ],
            options={
            },
            bases=('youthPlatform.advertisement',),
        ),
    ]

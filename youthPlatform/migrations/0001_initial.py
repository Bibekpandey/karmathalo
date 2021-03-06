# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Advertisement',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('institutionName', models.CharField(max_length=50)),
                ('institutionDistrict', models.CharField(max_length=20)),
                ('institutionLocation', models.CharField(max_length=30)),
                ('institutionContact', models.CharField(max_length=30)),
                ('institutionWebsite', models.CharField(blank=True, max_length=50)),
                ('institutionEmail', models.CharField(max_length=40)),
                ('description', models.TextField()),
                ('priority', models.IntegerField(default=3)),
                ('startDate', models.DateField(default=datetime.date.today)),
                ('endDate', models.DateField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Idea',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('title', models.CharField(max_length=150, default='title')),
                ('tags', models.CharField(max_length=150, default='')),
                ('isAnonymous', models.BooleanField(default=False)),
                ('description', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='JobAd',
            fields=[
                ('advertisement_ptr', models.OneToOneField(parent_link=True, auto_created=True, to='youthPlatform.Advertisement', primary_key=True, serialize=False)),
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
            name='Person',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
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
                ('person_ptr', models.OneToOneField(parent_link=True, auto_created=True, to='youthPlatform.Person', primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('accountType', models.IntegerField(default=1)),
                ('institution', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=('youthPlatform.person',),
        ),
        migrations.CreateModel(
            name='Qualification',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('level', models.CharField(max_length=20)),
                ('field', models.CharField(max_length=20)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TrainingAd',
            fields=[
                ('advertisement_ptr', models.OneToOneField(parent_link=True, auto_created=True, to='youthPlatform.Advertisement', primary_key=True, serialize=False)),
                ('duration', models.CharField(max_length=40)),
                ('cost', models.IntegerField()),
                ('givesJob', models.BooleanField(default=False)),
            ],
            options={
            },
            bases=('youthPlatform.advertisement',),
        ),
        migrations.AddField(
            model_name='idea',
            name='account',
            field=models.ForeignKey(to='youthPlatform.Account'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='advertisement',
            name='qualification',
            field=models.ManyToManyField(to='youthPlatform.Qualification'),
            preserve_default=True,
        ),
    ]

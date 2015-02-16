# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('youthPlatform', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Advertisement',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('institutionName', models.CharField(max_length=50)),
                ('institutionDistrict', models.CharField(max_length=20)),
                ('institutionLocation', models.CharField(max_length=30)),
                ('institutionContact', models.CharField(max_length=30)),
                ('institutionWebsite', models.CharField(blank=True, max_length=50)),
                ('institutionEmail', models.CharField(max_length=40)),
                ('detail', models.TextField()),
                ('priority', models.IntegerField(default=3)),
                ('startDate', models.DateTimeField(auto_now_add=True)),
                ('endDate', models.DateTimeField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Qualification',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('level', models.CharField(max_length=20)),
                ('field', models.CharField(max_length=20)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='advertisement',
            name='qualification',
            field=models.ManyToManyField(to='youthPlatform.Qualification'),
            preserve_default=True,
        ),
    ]

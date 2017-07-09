# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-08 20:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lighten',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('direction1', models.FloatField()),
                ('direction2', models.FloatField()),
                ('direction3', models.FloatField()),
                ('username', models.FloatField()),
                ('furniture_id', models.CharField(max_length=20)),
                ('furniture_type', models.CharField(max_length=20)),
                ('furniture_on', models.CharField(max_length=20)),
                ('furniture_off', models.CharField(max_length=20)),
            ],
            options={
                'ordering': ('direction1', 'direction2', 'direction3'),
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=80)),
                ('password', models.CharField(max_length=40)),
            ],
        ),
    ]
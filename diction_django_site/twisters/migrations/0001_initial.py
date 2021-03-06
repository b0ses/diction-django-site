# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-05 21:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Twister',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('twister', models.TextField(unique=True, verbose_name='tongue twister')),
                ('source', models.TextField(verbose_name='source url')),
            ],
            options={
                'db_table': 'twisters',
            },
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-06-17 16:37
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Documentos', '0013_auto_20160616_1538'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='archivo',
            name='publish',
        ),
    ]

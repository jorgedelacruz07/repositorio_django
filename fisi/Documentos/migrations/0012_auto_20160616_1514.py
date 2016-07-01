# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-06-16 20:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Documentos', '0011_auto_20160616_1124'),
    ]

    operations = [
        migrations.AddField(
            model_name='archivo',
            name='area',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Documentos.Area'),
        ),
        migrations.AddField(
            model_name='archivo',
            name='publish',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='archivo',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='archivo',
            name='updated',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]

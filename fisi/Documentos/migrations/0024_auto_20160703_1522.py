# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-07-03 20:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Documentos', '0023_auto_20160703_1518'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='votos',
            name='arch',
        ),
        migrations.RemoveField(
            model_name='votos',
            name='user',
        ),
        migrations.RemoveField(
            model_name='archivo',
            name='vot',
        ),
        migrations.AddField(
            model_name='archivo',
            name='votos',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.DeleteModel(
            name='votos',
        ),
    ]

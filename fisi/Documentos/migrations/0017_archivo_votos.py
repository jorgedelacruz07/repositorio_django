# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-06-19 00:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Documentos', '0016_auto_20160618_1406'),
    ]

    operations = [
        migrations.AddField(
            model_name='archivo',
            name='votos',
            field=models.IntegerField(null=True),
        ),
    ]
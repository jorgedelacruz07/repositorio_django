# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-06-24 18:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Documentos', '0019_comentario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comentario',
            name='comentario',
            field=models.TextField(max_length=500),
        ),
    ]

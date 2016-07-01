# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-06-18 18:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Documentos', '0014_remove_archivo_publish'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profesor',
            name='area',
        ),
        migrations.AddField(
            model_name='profesor',
            name='curso',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Documentos.curso'),
        ),
    ]

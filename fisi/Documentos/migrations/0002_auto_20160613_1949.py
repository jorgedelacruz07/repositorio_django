# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-06-14 00:49
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Documentos', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='documento',
            name='id',
        ),
        migrations.AlterField(
            model_name='documento',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL),
        ),
    ]

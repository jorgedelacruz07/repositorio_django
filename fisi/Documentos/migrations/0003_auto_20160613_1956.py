# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-06-14 00:56
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Documentos', '0002_auto_20160613_1949'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documento',
            name='nombre',
            field=models.CharField(max_length=50, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='documento',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-06-07 04:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inicio', '0008_plan_estudio'),
    ]

    operations = [
        migrations.AddField(
            model_name='alumno',
            name='plan',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='inicio.plan_estudio'),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-06-07 04:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inicio', '0007_auto_20160605_0409'),
    ]

    operations = [
        migrations.CreateModel(
            name='plan_estudio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plan', models.CharField(max_length=10)),
                ('eap', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inicio.EAP')),
            ],
        ),
    ]

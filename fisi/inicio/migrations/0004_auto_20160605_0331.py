# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-06-05 08:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inicio', '0003_auto_20160605_0048'),
    ]

    operations = [
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_departamento', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Distrito',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_distrito', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Provincia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_provincia', models.CharField(max_length=30)),
                ('departamento', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='inicio.Departamento')),
            ],
        ),
        migrations.AddField(
            model_name='distrito',
            name='provincia',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='inicio.Provincia'),
        ),
    ]

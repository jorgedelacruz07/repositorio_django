# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-06-16 16:10
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Documentos', '0007_auto_20160615_2104'),
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('area', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='curso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('curso', models.CharField(max_length=50)),
                ('area', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Documentos.Area')),
            ],
        ),
        migrations.CreateModel(
            name='cursoxprofesor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('area', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Documentos.Area')),
                ('curso', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Documentos.curso')),
            ],
        ),
        migrations.CreateModel(
            name='Profesor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('area', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Documentos.Area')),
            ],
        ),
        migrations.CreateModel(
            name='tipo_doc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=30)),
            ],
        ),
        migrations.AlterField(
            model_name='archivo',
            name='usuario',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]

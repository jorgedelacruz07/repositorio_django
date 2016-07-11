# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-07-03 20:18
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Documentos', '0022_comentario_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='votos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cant', models.IntegerField(blank=True, default=0, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='archivo',
            name='votos',
        ),
        migrations.AddField(
            model_name='votos',
            name='arch',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Documentos.Archivo'),
        ),
        migrations.AddField(
            model_name='votos',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='archivo',
            name='vot',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Documentos.votos'),
        ),
    ]
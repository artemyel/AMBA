# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-15 18:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0015_auto_20160815_2103'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='gender',
            field=models.CharField(choices=[('Мужчина', 'Мужчина'), ('Женщина', 'Женщина')], default='Мужчина', max_length=7),
        ),
    ]
# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-15 15:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='option_name',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='product',
            name='tag_line',
            field=models.CharField(default='', max_length=200),
        ),
    ]

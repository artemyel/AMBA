# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-20 16:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20160820_1617'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='short_name',
            field=models.CharField(default='', max_length=50),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-20 16:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_category_short_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='short_name',
            field=models.CharField(max_length=50, null=True),
        ),
    ]

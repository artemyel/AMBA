# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-20 16:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20160820_1648'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offer',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.CommunityProduct'),
        ),
    ]

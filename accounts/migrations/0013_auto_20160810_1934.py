# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-10 16:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0012_auto_20160810_1925'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='MyUsername',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='email',
            field=models.EmailField(error_messages={'blank': 'invalid', 'unique': 'HELLO'}, max_length=255, unique=True, verbose_name='email address'),
        ),
    ]
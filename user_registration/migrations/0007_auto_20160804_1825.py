# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-04 18:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_registration', '0006_auto_20160804_1823'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(null=True, upload_to='user_media'),
        ),
    ]

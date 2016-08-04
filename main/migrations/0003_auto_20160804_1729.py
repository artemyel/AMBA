# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-04 17:29
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0002_auto_20160715_1506'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('short_description', models.CharField(max_length=255, null=True)),
                ('price', models.SmallIntegerField()),
                ('meet_place', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='LotImages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='LotImages/')),
                ('is_main', models.BooleanField()),
                ('lot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Lot')),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='rating',
            field=models.SmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='lot',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Product'),
        ),
        migrations.AddField(
            model_name='lot',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]

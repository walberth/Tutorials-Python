# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2017-12-19 20:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0004_auto_20171219_1456'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurantlocation',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='restaurantlocation',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]

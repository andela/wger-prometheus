# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2017-09-12 09:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nutrition', '0002_auto_20170821_1802'),
    ]

    operations = [
        migrations.AddField(
            model_name='mealitem',
            name='meal_status',
            field=models.CharField(default='planned', max_length=10, verbose_name='Meal Status'),
        ),
    ]

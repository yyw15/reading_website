# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-27 02:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0004_note'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='time',
            field=models.CharField(default='', max_length=50),
        ),
    ]

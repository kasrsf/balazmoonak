# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-03-27 22:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='test',
            field=models.CharField(default=True, max_length=40, unique=True),
            preserve_default=False,
        ),
    ]

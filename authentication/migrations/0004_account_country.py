# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-03-28 22:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0003_auto_20160327_2208'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='country',
            field=models.CharField(choices=[('IR', 'ایران'), ('US', 'آمریکا')], default='IR', max_length=3),
        ),
    ]

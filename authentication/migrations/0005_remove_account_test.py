# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-03-28 22:51
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0004_account_country'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='test',
        ),
    ]

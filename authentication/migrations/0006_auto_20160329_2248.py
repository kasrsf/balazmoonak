# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-03-29 22:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0005_remove_account_test'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='username',
        ),
        migrations.AddField(
            model_name='account',
            name='first_name',
            field=models.CharField(default='t', max_length=40),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='account',
            name='gender',
            field=models.CharField(choices=[('M', 'مرد'), ('F', 'زن')], default='M', max_length=1),
        ),
        migrations.AddField(
            model_name='account',
            name='last_name',
            field=models.CharField(default='t', max_length=40),
            preserve_default=False,
        ),
    ]
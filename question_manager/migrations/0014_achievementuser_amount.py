# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-05-29 06:06
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('question_manager', '0013_auto_20160529_0604'),
    ]

    operations = [
        migrations.AddField(
            model_name='achievementuser',
            name='amount',
            field=models.PositiveIntegerField(default=1, validators=[django.core.validators.MinValueValidator(1)]),
            preserve_default=False,
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-05-09 16:36
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('question_manager', '0006_auto_20160509_1635'),
    ]

    operations = [
        migrations.AlterField(
            model_name='match',
            name='requested_score',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='requested_score', to='question_manager.Score'),
        ),
        migrations.AlterField(
            model_name='match',
            name='requested_user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='requested_user', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]

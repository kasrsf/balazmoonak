# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-05-09 17:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('question_manager', '0007_auto_20160509_1636'),
    ]

    operations = [
        migrations.AddField(
            model_name='match',
            name='category',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='question_manager.Category'),
            preserve_default=False,
        ),
    ]

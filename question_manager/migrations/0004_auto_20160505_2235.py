# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-05-05 22:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('question_manager', '0003_score'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'موضوع', 'verbose_name_plural': 'موضوع\u200cها'},
        ),
        migrations.AlterModelOptions(
            name='question',
            options={'verbose_name': 'سوال', 'verbose_name_plural': 'سوال\u200cها'},
        ),
        migrations.AlterModelOptions(
            name='score',
            options={'verbose_name': 'امتیاز', 'verbose_name_plural': 'امتیازها'},
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=20, verbose_name='نام'),
        ),
        migrations.AlterField(
            model_name='question',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='question_manager.Category', verbose_name='موضوع'),
        ),
        migrations.AlterField(
            model_name='question',
            name='choice2',
            field=models.TextField(verbose_name='گزینه دو'),
        ),
        migrations.AlterField(
            model_name='question',
            name='choice3',
            field=models.TextField(verbose_name='گزینه سه'),
        ),
        migrations.AlterField(
            model_name='question',
            name='choice4',
            field=models.TextField(verbose_name='گزینه چهار'),
        ),
        migrations.AlterField(
            model_name='question',
            name='question_text',
            field=models.TextField(verbose_name='متن سوال'),
        ),
        migrations.AlterField(
            model_name='question',
            name='right_answer',
            field=models.TextField(verbose_name='پاسخ صحیح'),
        ),
    ]
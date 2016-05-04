#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from authentication.models import Account

class Category(models.Model):
    name = models.CharField(max_length=20, verbose_name="نام")

    class Meta:
        verbose_name = "موضوع"
        verbose_name_plural = "موضوع‌ها"

    def __unicode__(self):
    	return self.name
    def __str__(self):
        return self.name


class Question(models.Model):
    question_text = models.TextField(null = False, verbose_name="متن سوال")
    right_answer = models.TextField(verbose_name="پاسخ صحیح")
    choice2 = models.TextField(verbose_name="گزینه دو")
    choice3 = models.TextField(verbose_name="گزینه سه")
    choice4 = models.TextField(verbose_name="گزینه چهار")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="موضوع")

    class Meta:
        verbose_name = "سوال"
        verbose_name_plural = "سوال‌ها"

    def __unicode__(self):
    	return self.question_text

    def __str__(self):
        return self.question_text

class Score(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    score = models.IntegerField()

    class Meta:
        verbose_name = "امتیاز"
        verbose_name_plural = "امتیازها"

    def __unicode__(self):
    	return self.score

    def __str__(self):
        return self.score

#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from authentication.models import Account
from enum import Enum
from django.core.validators import MinValueValidator
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
    	return str(self.score)

    def __str__(self):
        return str(self.score)

class Match(models.Model):
    category = models.ForeignKey(Category)
    starter_user = models.ForeignKey(Account, related_name='starter_user')
    requested_user = models.ForeignKey(Account, null=True, related_name='requested_user')
    starter_score = models.ForeignKey(Score, null=True, related_name='starter_score')
    requested_score = models.ForeignKey(Score, null=True, related_name='requested_score')
    q1 = models.ForeignKey(Question, related_name='q1')
    q2 = models.ForeignKey(Question, related_name='q2')
    q3 = models.ForeignKey(Question, related_name='q3')
    q4 = models.ForeignKey(Question, related_name='q4')
    q5 = models.ForeignKey(Question, related_name='q5')

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "مسابقه"
        verbose_name_plural = "مسابقه‌ها"

    def __unicode__(self):
    	return str(self.category)

    def __str__(self):
        return str(self.category)


class Achievement(models.Model):
    POINT = HOUR = 0
    CONSECUTIVE_WINS = DAY = 1
    MATCHS = WEEK = 2
    WINS = 3
    ACHIEVEMENT_TYPE = (
        (POINT, 'امتیاز'),
        (CONSECUTIVE_WINS, 'برد متوالی'),
        (MATCHS, 'بازی'),
        (WINS, 'برد'),
    )
    TIME_UNIT = (
        (HOUR, 'ساعت'),
        (DAY, 'روز'),
        (WEEK, 'هفته'),
    )
    type = models.IntegerField(choices = ACHIEVEMENT_TYPE, verbose_name="نوع دستاورد")
    amount = models.PositiveIntegerField(verbose_name = "میزان")
    time = models.IntegerField(default = 0, verbose_name= "بازه‌ی زمانی")
    time_unit = models.IntegerField(choices = TIME_UNIT, verbose_name = "نوع زمان")

    class Meta:
        verbose_name = "دستاورد"
        verbose_name_plural = "دستاوردها"

    def __unicode__(self):
    	return str(self.amount)

    def __str__(self):
        return str(self.amount)

class AchievementUser(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    achievement = models.ForeignKey(Achievement, on_delete = models.CASCADE)

    def __unicode__(self):
    	return str(self.achievement)

    def __str__(self):
        return str(self.achievement)

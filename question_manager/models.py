from __future__ import unicode_literals

from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=20)

    def __unicode__(self):
    	return self.name

    def __str__(self):
        return self.name


class Question(models.Model):
    question_text = models.TextField(null = False)
    right_answer = models.TextField()
    choice2 = models.TextField()
    choice3 = models.TextField()
    choice4 = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __unicode__(self):
    	return self.question_text

    def __str__(self):
        return self.question_text

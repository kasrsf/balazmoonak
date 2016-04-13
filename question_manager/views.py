from django.shortcuts import render
from django.http import HttpResponse
from .models import Question, Category, Score
from .serializers import CategorySerializer
from django.template import loader
from django.contrib.auth.decorators import login_required
from rest_framework import generics, permissions
from django.views import generic
from itertools import chain


from django.views.generic.base import TemplateView

class IndexView(generic.ListView):
    template_name = 'homepage.html'
    context_object_name = 'question_list'

    def get_queryset(self):
        return Question.objects.all()

class QuizCategorySelectView(generic.ListView):
    template_name = 'quiz_category_list.html'
    context_object_name = 'category_list'

    def get_queryset(self):
        return Category.objects.all()

class LeaderboardCategorySelectView(generic.ListView):
    template_name = 'leaderboard_category_list.html'
    context_object_name = 'category_list'

    def get_queryset(self):
        return Category.objects.all()


class QuizView(generic.ListView):
    template_name = 'quiz.html'
    context_object_name = 'questions'

    def get_queryset(self):
        return Question.objects.filter(category_id= self.kwargs.get('category_id', None)).order_by('?')[:3]

class LeaderboardView(generic.ListView):
    template_name = 'leaderboard.html'
    context_object_name = 'ranking'

    def get_queryset(self):
        category_id = self.kwargs.get('category_id', None)
        if category_id == '0':
            q1 = []
            q2 = Score.objects.order_by('-score')
        else:
            q1 = Category.objects.filter(id= category_id)
            q2 = Score.objects.filter(category_id=category_id).order_by('-score')
        return list(chain(q1, q2))

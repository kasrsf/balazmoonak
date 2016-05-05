from django.shortcuts import render
from django.http import HttpResponse
from .models import Question, Category, Score
from .serializers import CategorySerializer
from django.template import loader
from django.contrib.auth.decorators import login_required
from rest_framework import generics, permissions
from django.views import generic
from itertools import chain
from django.http import JsonResponse
from django.core import serializers
from django.views.generic.base import TemplateView
from django.views.decorators.csrf import csrf_exempt
import json

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

    def get_queryset(self):
        return []

class LeaderboardView(generic.ListView):
    template_name = 'leaderboard.html'
    context_object_name = 'ranking'

    def get_queryset(self):
        category_id = self.kwargs.get('category_id', None)
        if category_id == '0':
            q = Score.objects.order_by('-score')
        else:
            q = Score.objects.filter(category_id=category_id).order_by('-score')
        return q

    def post(self, request, *args, **kwargs):
        score = request.POST.get('score')
        user_id = request.POST.get('id')
        category_id = request.POST.get('category_id')

        s = Score(user_id=user_id, score=score, category_id=category_id)
        s.save()
        return HttpResponse('')

def questions(request, category_id):
    obj = Question.objects.filter(category_id= category_id).order_by('?')[:3]
    serialized_questions = serializers.serialize('json', obj)
    return HttpResponse(serialized_questions, content_type="application/json")

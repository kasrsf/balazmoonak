from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import *
from authentication.models import Account
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
    context_object_name = 'awaiting_matches'

    def get_queryset(self):
        return Match.objects.filter(requested_user_id=self.request.user.id, requested_score_id=None).count()

class QuizCategorySelectView(generic.ListView):
    template_name = 'quiz_category_list.html'
    context_object_name = 'category_list'

    def get_queryset(self):
        return Category.objects.all()

class MultiplayerQuizCategorySelectView(generic.ListView):
    template_name = 'mp_quiz_category_list.html'
    context_object_name = 'category_list'

    def get_context_data(self, **kwargs):
        context = super(MultiplayerQuizCategorySelectView, self).get_context_data(**kwargs)
        context['awaiting_matches'] = Match.objects.filter(requested_user_id=self.request.user.id, requested_score_id=None)
        return context

    def get_queryset(self):
        return Category.objects.all()

class MultiplayerModeSelectView(generic.ListView):
    template_name = 'mpquiz_mode.html'
    context_object_name = 'user_list'

    def get_queryset(self):
        user_id = self.request.user.id
        return Account.objects.exclude(id=user_id)


class LeaderboardCategorySelectView(generic.ListView):
    template_name = 'leaderboard_category_list.html'
    context_object_name = 'category_list'

    def get_queryset(self):
        return Category.objects.all()

class QuizView(generic.ListView):
    template_name = 'quiz.html'
    context_object_name = 'questions'

    def get_queryset(self):
        category_id = self.kwargs.get('category_id', None)
        return Question.objects.filter(category_id=category_id).order_by('?')[:5]


class OfflineMultiplayerQuizView(generic.ListView):
    template_name = 'offline_mpquiz.html'

    def get_context_data(self, **kwargs):
        context = super(OfflineMultiplayerQuizView, self).get_context_data(**kwargs)
        context['requested_user_id'] = self.kwargs.get('requested_user_id', None)
        return context

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

    def get_context_data(self, **kwargs):
        context = super(LeaderboardView, self).get_context_data(**kwargs)
        cat_id = (int)(self.kwargs.get('category_id', None))

        if (cat_id) == 0:
            context['category'] = "همه"
        else:
            context['category'] = Category.objects.get(id=cat_id).name
        return context

    def post(self, request, *args, **kwargs):
        qtype = request.POST.get('type')
        score = request.POST.get('score')
        user_id = request.POST.get('id')
        category_id = request.POST.get('category_id')

        s = Score(user_id=user_id, score=score, category_id=category_id)
        s.save()

        if qtype == "mp":
             requested_user = request.POST.get('requested')
             q1 = request.POST.get('q1')
             q2 = request.POST.get('q2')
             q3 = request.POST.get('q3')
             q4 = request.POST.get('q4')
             q5 = request.POST.get('q5')

             m = Match(starter_user_id=user_id, requested_user_id=requested_user,
                        starter_score_id=s.id, q1_id=q1, q2_id=q2, q3_id=q3,
                        q4_id=q4, q5_id=q5, category_id=category_id)
             m.save()
        elif qtype == "mpr":
            match_id = request.POST.get('match_id')
            Match.objects.filter(id=match_id).update(requested_score_id=s.id)
        elif qtype == "omp":
            match_id = request.POST.get('match_id')
            starter_id = Match.objects.filter(id=match_id).values('starter_user_id', 'requested_user_id')

            user_id = (int)(user_id);
            if (starter_id[0]['starter_user_id'] == user_id):
                Match.objects.filter(id=match_id).update(starter_score_id=s.id)
            elif (starter_id[0]['requested_user_id'] == user_id):
                Match.objects.filter(id=match_id).update(requested_score_id=s.id)

        return HttpResponse('')

def questions(request, category_id):
    obj = Question.objects.filter(category_id= category_id).order_by('?')[:5]
    serialized_questions = serializers.serialize('json', obj)
    return HttpResponse(serialized_questions, content_type="application/json")

def match_questions(request, match_id):
    match = Match.objects.get(id=match_id)

    serialized_questions = serializers.serialize('json', [match.q1, match.q2, match.q3, match.q4, match.q5])
    return HttpResponse(serialized_questions, content_type="application/json")

def available_matches(request, category_id):
    match = Match.objects.filter(category_id=category_id,
                                requested_user_id=None).exclude(starter_user_id=request.user.id)
    if match:
        match = match[0]
        serialized_questions = serializers.serialize('json', [match])
    else:
        match = None
        serialized_questions = []

    return HttpResponse(serialized_questions, content_type="application/json")

def check_match(request, category_id, match_id):
    match = Match.objects.filter(id=match_id).exclude(requested_user_id=None)

    if match:
        return JsonResponse({'status': 'y'})
    else:
        return HttpResponse('')

def online_score(request, match_id):
    match = Match.objects.get(id=match_id)
    user_id = request.user.id
    print(match.starter_user.id)
    if (match.starter_user.id == user_id):
        sc = match.requested_score.score
    elif (match.requested_user.id == user_id):
        sc = match.starter_score.score

    return JsonResponse({'score': sc})

class MultiplayerMatchmaker(generic.ListView):
    template_name = "matchmaker.html"

    def get_queryset(self):
        return []

    def get_context_data(self, **kwargs):
        context = super(MultiplayerMatchmaker, self).get_context_data(**kwargs)
        context['category_id'] = self.kwargs.get('category_id', None)
        return context

    def post(self, request, *args, **kwargs):
        mtype = request.POST.get('type')

        if mtype == "mch":
            user_id = request.POST.get('id')
            match_id = request.POST.get('match_id')
            Match.objects.filter(id=match_id).update(requested_user_id=user_id)
        elif mtype == "nm":
            user_id = request.POST.get('id')
            category_id = request.POST.get('category_id')

            questions = Question.objects.filter(category_id=category_id).values('id')
            m = Match(starter_user_id=user_id, q1_id=questions[0]['id'], q2_id=questions[1]['id']
                      , q3_id=questions[2]['id'], q4_id=questions[3]['id'],
                      q5_id=questions[4]['id'], category_id=category_id)
            m.save()

            return JsonResponse({'id': m.id})

        return HttpResponse('')

class OfflineMatchView(generic.ListView):
    template_name = "offline_mpquiz_reply.html"
    context_object_name = "opponent_score"

    def get_queryset(self):
        match_id = self.kwargs.get('match_id', None)
        return Match.objects.get(id=match_id)

class OnlineMatchView(generic.ListView):
    template_name = "online_mpquiz.html"

    def get_context_data(self, **kwargs):
        context = super(OnlineMatchView, self).get_context_data(**kwargs)
        context['match_id'] = self.kwargs.get('match_id', None)
        return context

    def get_queryset(self):
        return []

from django.conf.urls import url, include
from .serializers import CategorySerializer
from django.contrib.auth.decorators import login_required
from .views import *
from . import views

add_questions_urls = [
    url(r'^$', login_required(AddQuestionView.as_view()), name='add_question'),
    url(r'^$', login_required(QuizCategorySelectView.as_view()), name='category-list'),
]

single_player_quiz_urls = [
    url(r'^(?P<category_id>[0-9]+)/$', login_required(QuizView.as_view()), name='quiz-view'),
    url(r'^(?P<category_id>[0-9]+)/questions.json', views.questions, name='questions'),
	url(r'^$', login_required(QuizCategorySelectView.as_view()), name='category-list'),
]


multi_player_quiz_urls = [
    url(r'^(?P<category_id>[0-9]+)/$', login_required(MultiplayerModeSelectView.as_view()), name='mp-mode'),
    url(r'^(?P<category_id>[0-9]+)/(?P<match_id>[0-9]+)/check_match.json', login_required(views.check_match), name='checkmatch'),
    url(r'^(?P<category_id>[0-9]+)/(?P<requested_user_id>[0-9]+)/', login_required(OfflineMultiplayerQuizView.as_view()), name='off-quiz-view'),
    url(r'^(?P<category_id>[0-9]+)/findmatch', login_required(MultiplayerMatchmaker.as_view()), name='matchmaker'),
    url(r'^(?P<category_id>[0-9]+)/available_match.json', login_required(views.available_matches), name='getmatch'),
    url(r'^(?P<category_id>[0-9]+)/questions.json', views.questions, name='questions'),
    url(r'^$', login_required(MultiplayerQuizCategorySelectView.as_view()), name='mp-category-list'),
]

offline_match_urls = [
    url(r'^(?P<match_id>[0-9]+)/$', login_required(OfflineMatchView.as_view()), name='offline-match'),
    url(r'^(?P<match_id>[0-9]+)/questions.json$', views.match_questions, name='questions'),
]

online_match_urls = [
    url(r'^(?P<match_id>[0-9]+)/$', login_required(OnlineMatchView.as_view()), name='online-match'),
    url(r'^(?P<match_id>[0-9]+)/questions.json$', views.match_questions, name='questions'),
    url(r'^(?P<match_id>[0-9]+)/other_score.json$', views.online_score, name='score')
]

leaderboard_urls = [
    url(r'^$', login_required(LeaderboardCategorySelectView.as_view()), name='category-list'),
    url(r'^(?P<category_id>[0-9]+)/$', login_required(LeaderboardView.as_view()), name='leaderboard-view'),
]

urlpatterns = [
	url(r'^addquestions/', include(add_questions_urls)),
    url(r'^spquiz/', include(single_player_quiz_urls)),
    url(r'^mpquiz/', include(multi_player_quiz_urls)),
    url(r'^leaderboard/', include(leaderboard_urls)),
    url(r'^matches/', include(offline_match_urls)),
    url(r'^omatches/', include(online_match_urls)),
    url(r'^$', IndexView.as_view(), name = 'index'),
    url(r'^question/', views.question_add),
]

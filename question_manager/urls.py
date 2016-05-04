from django.conf.urls import url, include
from .serializers import CategorySerializer
from django.contrib.auth.decorators import login_required
from .views import IndexView, QuizCategorySelectView, LeaderboardCategorySelectView, QuizView, LeaderboardView
from . import views

single_player_quiz_urls = [
    url(r'^(?P<category_id>[0-9]+)/$', login_required(QuizView.as_view()), name='quiz-view'),
    url(r'^(?P<category_id>[0-9]+)/questions.json', views.questions, name='questions'),
    url(r'^result', views.post, name="result"),
	url(r'^$', login_required(QuizCategorySelectView.as_view()), name='category-list'),
]

leaderboard_urls = [
    url(r'^$', login_required(LeaderboardCategorySelectView.as_view()), name='category-list'),
    url(r'^(?P<category_id>[0-9]+)/$', login_required(LeaderboardView.as_view()), name='leaderboard-view'),
]

urlpatterns = [
	url(r'^spquiz/', include(single_player_quiz_urls)),
    url(r'^leaderboard/', include(leaderboard_urls)),
    url(r'^$', IndexView.as_view(), name = 'index'),
]

"""balazmoonak URL Configuration

"""
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import login
from django.contrib.auth.views import logout
from question_manager import views as qm_views
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('balazmoonak.account_urls')),
    url(r'', include('question_manager.urls')),
]

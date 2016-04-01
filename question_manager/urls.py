from django.conf.urls import url, include
from .serializers import CategorySerializer
from .views import CategoryList, CategoryDetail
from . import views

category_url = [
	url(r'^$', CategoryList.as_view(), name='category-list'),
	url(r'^(?P<pk>[0-9a-zA-Z_-]+)$', CategoryDetail.as_view(), name='category-detail'),
]

urlpatterns = [
	url(r'^$', views.IndexView.as_view(), name = 'index'),
	url(r'^category', include(category_url)),
]

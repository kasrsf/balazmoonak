from django.shortcuts import render
from django.http import HttpResponse
from .models import Question, Category
from .serializers import CategorySerializer
from django.template import loader
from django.contrib.auth.decorators import login_required
from rest_framework import generics, permissions
from django.views import generic


from django.views.generic.base import TemplateView

class IndexView(generic.ListView):
    template_name = 'homepage.html'
    context_object_name = 'question_list'

    def get_queryset(self):
        return Question.objects.all()

# @login_required (login_url='/accounts/login')
# def index(request):
# 	category_list = Category.objects.all()
# 	template = loader.get_template('homepage.html')
# 	context = { 'category_list' : category_list }
# 	return HttpResponse(template.render(context, request))

class CategoryList(generics.ListCreateAPIView):
	model = Category
	serializer_class = CategorySerializer
#	permission_classes = [
#		permissions.AllowAny
#	]
	def get_queryset(self):
		return Category.objects.all()

class CategoryDetail(generics.RetrieveAPIView):
    model = Category
    serializer_class = CategorySerializer

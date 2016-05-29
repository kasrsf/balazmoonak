from django.contrib import admin
from .models import Question, Category, Achievement
admin.site.register(Question)
admin.site.register(Category)
admin.site.register(Achievement)
# Register your models here.

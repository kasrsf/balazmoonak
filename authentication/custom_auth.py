from django.apps import apps
from question_manager import views

class AccountAdapter(allauth.adapter.DefaultAccountAdapter):

	def get_login_redirect_url(self, request):
		return '/dev'
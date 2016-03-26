from django.contrib.auth import get_user_model
from django import forms
class SignupForm(forms.Form):
	first_name = forms.CharField(max_length = 40, widget=forms.TextInput(attrs={'placeholder': 'First name'}))
	last_name = forms.CharField(max_length = 60, label = "last_name", widget=forms.TextInput(attrs={'placeholder': 'Last name'}))
	class Meta:
		model = get_user_model()
		fields = ['first_name', 'last_name']

	def signup(self, request, user):
		user.first_name = self.cleaned_data['first_name']
		user.last_name = self.cleaned_data['last_name']
		user.save()
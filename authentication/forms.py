from django.contrib.auth import get_user_model
from django import forms
from .models import Account
from allauth.account.forms import LoginForm
from captcha.fields import ReCaptchaField

farsi_errors = {
'required': 'تکمیل این فیلد اجباری است',
'invalid': 'مقدار وارد شده معتبر نیست'
}


class SignupForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(SignupForm, self).__init__(*args, **kwargs)
        self.fields['password1'].label = 'رمز عبور'
        self.fields['password1'].widget = forms.PasswordInput(attrs={'class': 'form-control'})
        self.fields['password1'].error_messages = farsi_errors;

        self.fields['password2'].label = 'تایید رمز'
        self.fields['password2'].widget = forms.PasswordInput(attrs={'class': 'form-control'})
        self.fields['password2'].error_messages = farsi_errors;

        self.fields['email'].label = 'E-mail'
        self.fields['email'].widget = forms.EmailInput(attrs={'class': 'form-control'})
        self.fields['email'].error_messages = farsi_errors;

    first_name = forms.CharField(label = "نام", widget=forms.TextInput(attrs={'class': 'form-control'}), error_messages=farsi_errors)
    last_name = forms.CharField(label = "نام خانوادگی", widget=forms.TextInput(attrs={'class': 'form-control'}), error_messages=farsi_errors)

    COUNTRIES = (("IR", "ایران"), ("US", "آمریکا"))
    country = forms.ChoiceField(choices=COUNTRIES, label = "کشور", widget=forms.Select(attrs={'class': 'form-control'}), error_messages = farsi_errors)

    GENDERS = (("M", "مرد"), ("F", "زن"))
    gender = forms.ChoiceField(choices=GENDERS, label = "جنسیت", widget=forms.Select(attrs={'class': 'form-control'}), error_messages=farsi_errors)

    def signup(self, request, user):
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.country = self.cleaned_data['country']
        user.gender = self.cleaned_data['gender']
        user.save()


class LoginForm(LoginForm):
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.fields['login'].widget = forms.EmailInput(attrs={'label': 'ایمیل','class': 'form-control'})
        self.fields['login'].label = 'E-mail'
        self.fields['login'].error_messages = farsi_errors;

        self.fields['password'].label = 'رمز عبور'
        self.fields['password'].widget = forms.PasswordInput(attrs={'class': 'form-control'})
        self.fields['password'].error_messages = farsi_errors;

        self.fields['captcha'] = ReCaptchaField(label='', attrs={'width' : '50%'})

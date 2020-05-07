# -*- coding: utf-8 -*- 
"""
Django settings for balazmoonak project.

Generated by 'django-admin startproject' using Django 1.9.4.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = 'SECRET_KEY'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
	'rest_framework',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
	'question_manager.apps.QuestionManagerConfig',
	'django.contrib.sites',
	'allauth',
	'allauth.account',
	'allauth.socialaccount',
	'authentication',
    'captcha',
    'django_countries',
]

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'balazmoonak.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
				'django.template.context_processors.request',
            ],
        },
    },
]

WSGI_APPLICATION = 'balazmoonak.wsgi.application'
#STATICFILES_DIRS = (
#    os.path.join(BASE_DIR, 'static'),
#	)

# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
		'NAME' : 'balazmoonak',
		'USER' : 'balazmoonak',
		'PASSWORD' : '1234',
		'HOST' : 'localhost',
		'PORT' : '',
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'fa'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True
####AUTH
AUTHENTICATION_BACKENDS = (

    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',
#
#    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
#
)


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/
STATIC_URL = '/static/'
#ACCOUNT_EMAIL_REQUIRED (=False)
SITE_ID = 1
try:
    from local_settings import *
except ImportError:
	pass

AUTH_USER_MODEL = 'authentication.Account'

# django-allauth Configuration variables you might like to change.
#
# DO NOT CHANGE THIS FILE. Instead, copy it to local_settings.py
# and make your changes there.


# Specifies the login method to use -- whether the user logs in by entering
# their username, e-mail address, or either one of both. Possible values
# are 'username' | 'email' | 'username_email'
ACCOUNT_AUTHENTICATION_METHOD = 'email'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'balazmoonak@gmail.com'
EMAIL_HOST_PASSWORD = 'balazmoonak123'
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

# The URL to redirect to after a successful e-mail confirmation, in case no
# user is logged in. Default value is settings.LOGIN_URL.
# ACCOUNT_EMAIL_CONFIRMATION_ANONYMOUS_REDIRECT_URL
ACCOUNT_SIGNUP_FORM_CLASS = 'authentication.forms.SignupForm'
ACCOUNT_FORMS = {'login': 'authentication.forms.LoginForm'}
#ACCOUNT_ADAPTER = 'authentication.custom_auth.AccountAdapter'
ACCOUNT_LOGOUT_REDIRECT_URL = '/'
LOGIN_REDIRECT_URL = '/'

# The URL to redirect to after a successful e-mail confirmation, in case of
# an authenticated user. Default is settings.LOGIN_REDIRECT_URL
# ACCOUNT_EMAIL_CONFIRMATION_AUTHENTICATED_REDIRECT_URL

# Determines the expiration date of email confirmation mails (# of days).
# ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS = 3

# The user is required to hand over an e-mail address when signing up.
ACCOUNT_EMAIL_REQUIRED = True

# Determines the e-mail verification method during signup. When set to
# "mandatory" the user is blocked from logging in until the email
# address is verified. Choose "optional" or "none" to allow logins
# with an unverified e-mail address. In case of "optional", the e-mail
# verification mail is still sent, whereas in case of "none" no e-mail
# verification mails are sent.
ACCOUNT_EMAIL_VERIFICATION = "mandatory"

# Subject-line prefix to use for email messages sent. By default, the name
# of the current Site (django.contrib.sites) is used.
# ACCOUNT_EMAIL_SUBJECT_PREFIX = '[Site] '

# A string pointing to a custom form class
# (e.g. 'myapp.forms.SignupForm') that is used during signup to ask
# the user for additional input (e.g. newsletter signup, birth
# date). This class should implement a `def signup(self, request, user)`
# method, where user represents the newly signed up user.
# ACCOUNT_SIGNUP_FORM_CLASS = None

# When signing up, let the user type in their password twice to avoid typ-o's.
# ACCOUNT_SIGNUP_PASSWORD_VERIFICATION = True

# Enforce uniqueness of e-mail addresses.
# ACCOUNT_UNIQUE_EMAIL = True

# A callable (or string of the form 'some.module.callable_name') that takes
# a user as its only argument and returns the display name of the user. The
# default implementation returns user.username.
# ACCOUNT_USER_DISPLAY

# An integer specifying the minimum allowed length of a username.
# ACCOUNT_USERNAME_MIN_LENGTH = 1

# The user is required to enter a username when signing up. Note that the
# user will be asked to do so even if ACCOUNT_AUTHENTICATION_METHOD is set
# to email. Set to False when you do not wish to prompt the user to enter a
# username.
ACCOUNT_USER_MODEL_USERNAME_FIELD = None
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_SESSION_REMEMBER = False
ACCOUNT_LOGOUT_ON_GET = True
ACCOUNT_LOGIN_ON_EMAIL_CONFIRMATION = True

# render_value parameter as passed to PasswordInput fields.
# ACCOUNT_PASSWORD_INPUT_RENDER_VALUE = False

# An integer specifying the minimum password length.
ACCOUNT_PASSWORD_MIN_LENGTH = 4

# Request e-mail address from 3rd party account provider? E.g. using OpenID
# AX, or the Facebook 'email' permission.
# SOCIALACCOUNT_QUERY_EMAIL = ACCOUNT_EMAIL_REQUIRED

# Attempt to bypass the signup form by using fields (e.g. username, email)
# retrieved from the social account provider. If a conflict arises due to a
# duplicate e-mail address the signup form will still kick in.
# SOCIALACCOUNT_AUTO_SIGNUP = True

# Enable support for django-avatar. When enabled, the profile image of the
# user is copied locally into django-avatar at signup. Default is
# 'avatar' in settings.INSTALLED_APPS.
# SOCIALACCOUNT_AVATAR_SUPPORT

# Dictionary containing provider specific settings.
# SOCIALACCOUNT_PROVIDERS

## RECAPTCHA settings
RECAPTCHA_PUBLIC_KEY = '6LfTDRwTAAAAAO4pl3QLObwIzr2iBa58I0aL0AX6'
#RECAPTCHA_PRIVATE_KEY = 'PRIVATE_KEY'

RECAPTCHA_USE_SSL = True

STATIC_ROOT = os.path.join(BASE_DIR, "static/")

COUNTRIES_OVERRIDE = {
    'IR': 'ایران'
}

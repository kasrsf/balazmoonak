# -*- coding: utf-8

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin, Group
from django.db import models
from django.contrib.contenttypes.models import ContentType


class AccountManager(BaseUserManager):
    def create_user(self, email, password, first_name, last_name, country, gender, **kwargs):
        if not email:
            raise ValueError('Users must have a valid email address.')

        account = self.model(
            email=self.normalize_email(email), first_name = first_name, last_name = last_name,
            country = country
        )

        account.set_password(password)
        account.save()

        return account

    def create_superuser(self, email, password, **kwargs):
        account = self.create_user(email=email, password=password, first_name="", last_name="", country="", gender="", **kwargs)

        account.is_superuser = True
        account.save()

        return account

class Account(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    email = models.EmailField(unique=True)

    GENDERS = (("M", "مرد"), ("F", "زن"))
    gender = models.CharField(choices=GENDERS, default="M", max_length=1)

    COUNTRIES = (("IR", "ایران"), ("US", "آمریکا"))
    country = models.CharField(choices=COUNTRIES, default="IR", max_length=3)
    is_admin = models.BooleanField(default=False)

    objects = AccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


    def get_full_name(self):
        # The user is identified by their email address
        return self.email

    def get_short_name(self):
        # The user is identified by their email address
        return self.email

    @property
    def is_staff(self):
        return True
    def __unicode__(self):
        return self.email

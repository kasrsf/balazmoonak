from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models

class AccountManager(BaseUserManager):
    def create_user(self, email, password, first_name, last_name, country, gender, **kwargs):
        if not email:
            raise ValueError('Users must have a valid email address.')

        if not kwargs.get('username'):
            raise ValueError('Users must have a valid username.')

        account = self.model(
            email=self.normalize_email(email), first_name = first_name, last_name = last_name,
            country = country
        )

        account.is_admin = True

        account.set_password(password)
        account.save()

        return account

    def create_superuser(self, email, password, first_name, last_name, country, gender, **kwargs):
        account = self.create_user(email, password, first_name, last_name, country, gender, **kwargs)

        #account.is_admin = True
        account.save()

        return account

class Account(AbstractBaseUser):
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

    def __unicode__(self):
        return self.email

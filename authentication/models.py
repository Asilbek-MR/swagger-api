from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField

class CustomUserManager(BaseUserManager):
    def create_user(self,email,password,**extra_fields):
        if not email:
            raise ValueError(_('Please enter an email address'))
        email=self.normalize_email(email)
        new_user=self.model(email=email,**extra_fields)
        new_user.set_password(password)
        new_user.save()
        return new_user

    def create_superuser(self,email,password,**extra_fields):
        extra_fields.setdefault('is_superuser',True)
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_active',True)

        if extra_fields.get('is_superuser') is not True:

            raise(_('Superuser must have is_superuser=true'))

        if extra_fields.get('is_staff') is not True:

            raise(_('Superuser must have is_staff=true'))

        return self.create_user(email,password,**extra_fields)

class User(AbstractUser):
    username=models.CharField(_('Username'),max_length=40,unique=True)
    email=models.CharField(_('Email'), max_length=80,unique=True)
    phone_number=PhoneNumberField(unique=True,null=False,blank=True)
    date_joined=models.DateTimeField(_('Date'),auto_now_add=True)

    REQUIRED_FIELDS=['username','phone_number']
    USERNAME_FIELD='email'

    def __str__(self):
        return f"User {self.username}"




























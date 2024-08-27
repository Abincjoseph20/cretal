#from django.db import models
# from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
#
# class MyAccountManager(BaseUserManager):
#     def create_user(self, first_name, last_name, username, email, password=None):
#         if not email:
#             raise ValueError('User must have an email address')
#
#         if not username:
#             raise ValueError('User must have a username')
#
#         user = self.model(
#             email=self.normalize_email(email),
#             username=username,
#             first_name=first_name,
#             last_name=last_name,
#         )
#         user.set_password(password)
#         user.save(using=self._db)
#         return user
#
#     def create_superuser(self, first_name, last_name, username, email, password):
#         user = self.create_user(
#             email=self.normalize_email(email),
#             username=username,
#             password=password,
#             first_name=first_name,
#             last_name=last_name,
#         )
#         user.is_admin = True
#         user.is_active = True
#         user.is_staff = True
#         user.is_superadmin = True
#         user.save(using=self._db)
#         return user
#
#
# class Account(AbstractBaseUser):
#     first_name = models.CharField(max_length=60)
#     last_name = models.CharField(max_length=60)
#     username = models.CharField(max_length=60, unique=True)
#     email = models.EmailField(max_length=100, unique=True)
#     phone_number = models.CharField(max_length=20)
#
#     date_joined = models.DateTimeField(auto_now_add=True)
#     last_login = models.DateTimeField(auto_now=True)
#     is_admin = models.BooleanField(default=False)
#     is_staff = models.BooleanField(default=False)
#     is_active = models.BooleanField(default=False)
#     is_superadmin = models.BooleanField(default=False)
#
#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ['username', 'first_name', 'last_name']
#
#     objects = MyAccountManager()
#
#     def __str__(self):
#         return self.email
#
#     def has_perm(self, perm, obj=None):
#         return self.is_admin
#
#     def has_module_perms(self, app_label):
#         return True
# class Order(models.Model):
#     account = models.ForeignKey(Account, on_delete=models.PROTECT)
#     # other fields



# from django.urls import reverse
# from django import forms
# from django.db.models.signals import post_delete
# from django.utils import timezone
# from decimal import Decimal
# from django.db.models.signals import pre_save
# from django.dispatch import receiver
# import logging
# from django.core.files.storage import default_storage
# from django.core.files import File
# import random
# import string

#from django.conf import settings

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class User_manager(BaseUserManager):
    def create_user(self, email, username, first_name, last_name, mobile, password=None):
        if not email:
            raise ValueError('User must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            username=username,
            first_name=first_name,
            last_name=last_name,
            mobile=mobile
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, first_name, last_name, mobile, password):
        user = self.create_user(
            email=self.normalize_email(email),
            password=password,
            username=username,
            first_name=first_name,
            last_name=last_name,
            mobile=mobile
        )

        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.is_superadmin = True
        user.save(using=self._db)
        return user

    def get_by_natural_key(self, email):
        return self.get(email=email)

class User(AbstractBaseUser):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    mobile = models.CharField(max_length=50, unique=True)

    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now_add=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_blocked = models.BooleanField(default=False)
    is_superadmin = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'mobile', 'first_name', 'last_name']

    objects = User_manager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, add_label):
        return True
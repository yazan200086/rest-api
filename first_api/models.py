from django.db import models

from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager




class UserProfileManger(BaseUserManager):
    '''manger for the next class'''
    def create_user(self,email,name,password=None):
        if not email:
            raise ValueError ('user must have email')
        email =self.normalize_email(email)
        user=self.model(email=email,name=name)
        user.set_password(password)   #Good practice not field in the DB
        user.save(using=self._db)

        return user

    def create_superuser(self,email,name,password):
        user=self.create_user(email,name,password)
        user.is_superuser=True
        user.is_staff=True
        user.save(using=self.db)
        return user





class UserProfile(AbstractBaseUser,PermissionsMixin):
    """model database for user"""
    email = models.EmailField(max_length=255,unique=True)
    name = models.CharField(max_length=255)
    is_active=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=False)
    objects=UserProfileManger()


    USERNAME_FIELD='email'
    REQUIRED_FIELDS =['name']

    def get_full_name(self):
        return self.name

    def __str__(self):
        '''retuen str represntation of the user'''
        return self.email

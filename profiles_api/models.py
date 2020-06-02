from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

# Create your models here.


class UserProfileManager(BaseUserManager):
    '''Manager for user profile'''
    def create_user(self, email, name, password=None):
        '''create a new user profile'''
        


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """database models for user of the system"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    object = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """retrieve full name of user"""
        return self.name

    def get_short_name(self):
        """retrieve short name of user"""
        return self.name

    def __str__(self):
        """return string representation of user"""
        return self.email

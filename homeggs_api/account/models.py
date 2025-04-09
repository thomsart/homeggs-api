from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser
from django.db import models

from .managers import UserManager


class User(AbstractUser):
    """
    User model in account app.
    """

    username = None
    email = models.EmailField('email address', unique=True)
    phone = models.CharField(max_length=15)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [] # cette variable donne les champs supplementaires 
                         # obligatoires lors de la creation du superuser 

    objects = UserManager()

    def __str__(self):
        return self.first_name + " " + self.last_name

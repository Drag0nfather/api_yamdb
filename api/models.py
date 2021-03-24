from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = models.CharField(max_length=20, unique=True)
    bio = models.CharField(max_length=500)
    email = models.EmailField(unique=True)
    role = models.TextChoices(value='user', names='user, admin, moderator')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ('username',)

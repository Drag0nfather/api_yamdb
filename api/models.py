from django.contrib.auth.models import AbstractUser
from django.db import models

from api.mail import generate_confirm_code


class User(AbstractUser):
    username = models.CharField(max_length=20, unique=True)
    bio = models.CharField(max_length=500)
    email = models.EmailField(unique=True)
    role = models.TextChoices(value='user', names='user, admin, moderator')
    confirmation_code = models.CharField(max_length=6, null=True, default=generate_confirm_code)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ('username',)

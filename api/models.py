from django.contrib.auth.models import AbstractUser
from django.db import models

from api.mail import generate_confirm_code


class Categories(models.Model):
    search = models.CharField(
        max_length=50,
        blank=True, null=True,
        verbose_name='Категории',
        help_text='Поиск по категории',
    )

    class Meta:
        verbose_name = 'Categories'
        verbose_name_plural = 'Categories'


class Genres(models.Model):
    search = models.CharField(
        max_length=50,
        blank=True, null=True,
        verbose_name='Жанры',
        help_text='Поиск по жанрам',
    )

    class Meta:
        verbose_name = 'Genres'
        verbose_name_plural = 'Genres'


class Title(models.Model):
    category = models.CharField(
        max_length=50,
        blank=True, null=True,
        verbose_name='Категория',
        help_text='Категория тайтла',
    )
    genre = models.CharField(
        max_length=50,
        blank=True, null=True,
        verbose_name='Жанр',
        help_text='Жанр тайтла',
    )
    name = models.CharField(
        max_length=50,
        blank=True, null=True,
        verbose_name='Имя',
        help_text='Имя тайтла',
    )
    year = models.DateField(
        verbose_name='Год',
        help_text='Год выпуска тайтла',
    )

    class Meta:
        verbose_name = 'Title'
        verbose_name_plural = 'Title'


class Roles(models.TextChoices):
    USER = 'user'
    MODERATOR = 'moderator'
    ADMIN = 'admin'


class User(AbstractUser):

    class Meta:
        ordering = ['-id']

    username = models.CharField(max_length=30, unique=True,
                                blank=False, null=False)
    bio = models.CharField(max_length=4000, null=True)
    email = models.EmailField(max_length=255, unique=True,
                              blank=False, null=False)
    role = models.CharField(max_length=50, choices=Roles.choices)
    confirmation_code = models.CharField(max_length=6, null=True, default=generate_confirm_code)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ('username',)

    @property
    def is_admin(self):
        return self.is_staff or self.role == Roles.ADMIN

    @property
    def is_moderator(self):
        return self.role == Roles.MODERATOR

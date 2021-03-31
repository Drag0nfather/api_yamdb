from django.contrib.auth.models import AbstractUser
from django.db import models

from api.mail import generate_confirm_code


class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name


class Title(models.Model):
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True, blank=True,
        related_name='titles',
    )
    genre = models.ManyToManyField(
        Genre,
        null=True, blank=True,
        related_name='titles',
    )
    name = models.CharField(max_length=50)
    year = models.PositiveIntegerField()
    description = models.TextField()

    def __str__(self):
        return self.name


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
    confirmation_code = models.CharField(
        max_length=6,
        null=True,
        default=generate_confirm_code
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ('username',)

    @property
    def is_admin(self):
        return self.is_staff or self.role == Roles.ADMIN

    @property
    def is_moderator(self):
        return self.role == Roles.MODERATOR


class Review(models.Model):
    RATING_RANGE = (
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
        (6, 6),
        (7, 7),
        (8, 8),
        (9, 9),
        (10, 10)
    )
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='reviews'
    )
    pub_date = models.DateTimeField(auto_now_add=True)
    score = models.IntegerField(choices=RATING_RANGE)
    text = models.TextField(max_length=5000)
    title = models.ForeignKey(
        Title, on_delete=models.CASCADE, related_name='reviews'
    )

    def __str__(self):
        return self.text


class Comment(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='comments'
    )
    pub_date = models.DateTimeField(auto_now_add=True)
    review = models.ForeignKey(
        Review, on_delete=models.CASCADE, related_name='comments'
    )
    text = models.TextField(max_length=500)

    def __str__(self):
        return self.text

from django.db import models


# TODO: Reviews, Commemnts
class Categories(models.Model):
    search = models.CharField()

    class Meta:
        verbose_name = 'Категории'
        ordering = ['name']


class Genres(models.Model):
    search = models.CharField()

    class Meta:
        verbose_name = 'Жанры'
        ordering = ['name']


class Title(models.Model):
    category = models.CharField()
    genre = models.CharField()
    name = models.CharField()
    year = models.DateField()

    class Meta:
        verbose_name = 'Название фильма'
        ordering = ['name']

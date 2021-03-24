from django.db import models


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
        # ordering = ['-pub_date']


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
        # ordering = ['-pub_date']


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
        # ordering = ['-pub_date']


# class Reviews(models.Model):
#     title_id = models.ForeignKey(
#         Title,
#         on_delete=models.CASCADE,
#         verbose_name='Отзывы',
#         help_text='Отзывы к тайтлу',
#         related_name='Title'
#     )

#     class Meta:
#         verbose_name = 'Reviews'
#         verbose_name_plural = 'Reviews'
#         # ordering = ['-pub_date']


# class Comments(models.Model):
#     title_id = models.ForeignKey(
#         Title,
#         on_delete=models.CASCADE,
#         verbose_name='Комментарии',
#         help_text='Комментарии к тайтлу',
#     )
#     review_id = models.ForeignKey(
#         Reviews,
#         on_delete=models.CASCADE,
#         verbose_name='Отзывы',
#         help_text='Отзывы к тайтлу',
#     )
#     class Meta:
#         verbose_name = 'Comments'
#         verbose_name_plural = 'Comments'

from django.db import models
from django.contrib.auth.models import User


class Genre(models.Model):
    name = models.CharField(max_length=200, verbose_name="Название")

    class Meta:
        verbose_name = 'жанр'
        verbose_name_plural = 'жанры'

    def __str__(self):
        return self.name


class Director(models.Model):
    name = models.CharField(max_length=200, verbose_name="ФИО")

    class Meta:
        verbose_name = 'режисер'
        verbose_name_plural = 'режисеры'

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=200, verbose_name="Название")
    director = models.ForeignKey(
        Director,
        verbose_name='режисер',
        related_name='movie',
        null=True,
        on_delete=models.SET_NULL,
    )
    release_year = models.IntegerField(verbose_name="Год выпуска")
    genre = models.ForeignKey(
        Genre,
        verbose_name='жанр',
        related_name='movie',
        null=True,
        on_delete=models.SET_NULL,
    )
    rating = models.FloatField(
        default=0,
        choices=[(i / 2, str(i / 2)) for i in range(0, 11)],
        verbose_name="Рейтинг (0–5)"
    )
    poster = models.ImageField(blank=True, null=True, verbose_name="Обложка")
    description = models.TextField(blank=True, verbose_name="Описание")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'фильм'
        verbose_name_plural = 'фильмы'

    def __str__(self):
        return f"{self.title} ({self.release_year})"
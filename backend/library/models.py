from datetime import datetime

from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator


class Author(models.Model):
    name = models.CharField(
        'Имя автора',
        max_length=50)
    birthday = models.DateField('Дата рождения')
    biography = models.TextField('Краткая биография')

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'

    def __str__(self):
        return f'{self.name}'


class Book(models.Model):
    name = models.CharField(
       'Название книги',
       max_length=100
    )
    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
        related_name='books',
        verbose_name='Автор(ы)'
    )
    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='books',
    )
    year_of_publication = models.IntegerField(
        'Год публикации',
        max_length=4,
        validators=[
            MinValueValidator(618),
            MaxValueValidator(datetime.now().year)
        ]
    )
    description = models.TextField('Краткое описание')
    image = models.ImageField(
        'Изображение обложки',
        upload_to='covers/'
    )

    class Meta:
        ordering = ['id']
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'
        unique_together = [['name', 'author']]

    def __str__(self):
        return f'{self.name}'


class Review(models.Model):
    text = models.TextField('Текст отзыва')
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='reviews',
    )
    book = models.ForeignKey(
        Book,
        on_delete=models.CASCADE,
        related_name='reviews',
    )

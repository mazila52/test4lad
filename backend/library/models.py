from django.db import models


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
    author = models.ManyToManyField(
        Author,
        verbose_name='Автор(ы)'
    )
    year_of_publication = models.IntegerField('Год публикации')
    description = models.TextField('Краткое описание')
    image = models.ImageField(
        'Изображение обложки',
        upload_to='covers/'
    )

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'

    def __str__(self):
        return f'{self.name}'
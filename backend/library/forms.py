from django import forms

from .models import Book, Review


class BookForm(forms.ModelForm):

    class Meta:
        model = Book
        fields = (
            'name',
            'author',
            'year_of_publication',
            'description',
            'image',
        )
        labels = {
            'name': 'Название',
            'author': 'Автор',
            'year_of_publication': 'Год издания',
            'description': 'Краткое описание',
            'image': 'Картинка',
        }


class ReviewForm(forms.ModelForm):

    class Meta:
        model = Review
        fields = ('text',)

from django.urls import include, path

from .views import RegisterUser, index, book_detail

app_name = 'library'

urlpatterns = [
    path('', index, name='index'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('library/book/<int:book_id>', book_detail, name='book_deatil')
]
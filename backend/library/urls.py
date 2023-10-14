from django.urls import path

from . import views

app_name = 'library'

urlpatterns = [
    path('', views.BookList.as_view(), name='index'),
    path('register/', views.RegisterUser.as_view(), name='register'),
    path(
        'library/book/<int:pk>/',
        views.BookDetail.as_view(),
        name='book_detail'
    ),
    path(
        'library/book/<int:pk>/edit/',
        views.BookUpdate.as_view(),
        name='book_edit'
    ),
    path(
        'library/book/<int:pk>/delete/',
        views.BookDelete.as_view(),
        name='book_delete'

    ),
    path(
        'library/book/create/',
        views.BookCreate.as_view(),
        name='book_create'
    ),
    path(
        'library/book/search/',
        views.SearchBook.as_view(),
        name='book_search'
    ),
    path(
        'library/book/<int:pk>/review/',
        views.AddReview.as_view(),
        name='book_review'
    ),
]

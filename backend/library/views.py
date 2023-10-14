from django.db.models import Q
from django.http import HttpResponseBadRequest, HttpResponse
from django.contrib.auth import get_user_model
from django.views.generic import CreateView, ListView, DetailView, DeleteView
from django.views.generic.base import View
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect

from .models import Book, Review
from .forms import BookForm, ReviewForm

User = get_user_model()


class RegisterUser(CreateView):
    form_class = UserCreationForm
    template_name = "registration/registration.html"
    success_url = reverse_lazy('library:index')


class BookList(ListView):
    paginate_by = 3
    model = Book
    template_name = 'library/index.html'
    context_object_name = 'books'


class BookDetail(DetailView):
    model = Book
    template_name = 'library/book_detail.html'

    def get_context_data(self, **kwargs):
        context = super(BookDetail, self).get_context_data(**kwargs)
        pk = self.kwargs.get('pk')
        reviews = Review.objects.filter(book_id=pk)
        context['reviews'] = reviews
        return context


class BookDelete(LoginRequiredMixin, DeleteView):
    model = Book
    success_url = reverse_lazy('library:index')
    login_url = '/auth/login/'

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        book = get_object_or_404(Book, id=self.kwargs.get('pk'))
        if book.user != request.user:
            return HttpResponse('Нельзя удалить чужую книгу', status=301)
        self.object.delete()
        return redirect(self.get_success_url())


class BookUpdate(LoginRequiredMixin, UpdateView):
    login_url = '/auth/login/'
    from_class = BookForm
    model = Book
    fields = (
        'name',
        'author',
        'year_of_publication',
        'description',
        'image',
    )
    template_name = 'library/book_create.html'
    success_url = reverse_lazy('library:index')

    def form_valid(self, form):
        if form.instance.user == self.request.user:
            return super().form_valid(form)
        return HttpResponse('Нельзя редактировать чужую книгу', status=301)


class BookCreate(LoginRequiredMixin, CreateView):
    login_url = '/auth/login/'
    form_class = BookForm
    template_name = 'library/book_create.html'
    success_url = reverse_lazy('library:index')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class SearchBook(ListView):

    context_object_name = 'books'
    template_name = 'library/book_search.html'

    def get_queryset(self):
        return Book.objects.filter(
            Q(name__icontains=self.request.GET.get('q')) |
            Q(author__name__icontains=self.request.GET.get('q'))
        )


class AddReview(View):

    def post(self, request, pk):
        print(request.POST)
        form = ReviewForm(request.POST)
        book = get_object_or_404(Book, id=pk)
        user = get_object_or_404(User, username=request.user)
        if form.is_valid():
            form = form.save(commit=False)
            form.book = book
            form.author = user
            form.save()
            return redirect(
                reverse_lazy('library:book_detail', kwargs={'pk': pk})
            )
        return HttpResponseBadRequest()

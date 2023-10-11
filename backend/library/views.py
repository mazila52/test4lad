from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm

from .models import Book
from django.shortcuts import get_object_or_404

def index(request):
    post_list = Book.objects.all()
    #paginator = Paginator(post_list, settings.GLOBAL_SETTINGS['post_on_page'])
    #page_number = request.GET.get('page')
    #page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': post_list,
    }
    return render(request, 'library/index.html', context)

def book_detail(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    context = {
        'book': book,
    }
    return render(request, 'library/book_detail.html', context)
class RegisterUser(CreateView):
    form_class = UserCreationForm
    template_name = "registration/registration.html"
    success_url = reverse_lazy('library:index')

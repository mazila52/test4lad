from rest_framework import viewsets

from .serialisers import AuthorSerializer
from library.models import Author

class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

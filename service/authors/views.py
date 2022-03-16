from rest_framework.viewsets import ModelViewSet

from authors.models import Author
from authors.serializers import AuthorModelSerializer


class AuthorModelViewSet():
    queryset = Author.objects.all()
    serializer_class = AuthorModelSerializer

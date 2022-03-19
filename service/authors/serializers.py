from rest_framework.serializers import HyperlinkedModelSerializer

from authors.models import Author, Book, Article, Biography


class AuthorModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'


class BookModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'


class ArticleModelSerializer(HyperlinkedModelSerializer):
    author = AuthorModelSerializer()

    class Meta:
        model = Article
        fields = '__all__'


class BiographyModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Biography
        fields = '__all__'

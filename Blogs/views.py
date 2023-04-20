from rest_framework import viewsets
from django_elasticsearch_dsl_drf.filter_backends import (
    FilteringFilterBackend,
    SearchFilterBackend,
    OrderingFilterBackend,
)
from django_elasticsearch_dsl_drf.viewsets import DocumentViewSet
from .models import Category, Author, Article
from .serializers import CategorySerializer, AuthorSerializer, ArticleSerializer
from .documents import ArticleDocument

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class ArticleViewSet(DocumentViewSet):
    document = ArticleDocument
    serializer_class = ArticleSerializer
    filter_backends = [
        FilteringFilterBackend,
        SearchFilterBackend,
        OrderingFilterBackend,
    ]
    search_fields = (
        'title',
        'content',
        'category.name',
        'author.name',
    )
    filter_fields = {
        'category': 'category.name',
        'author': 'author.name',
    }
    ordering_fields = {
        'title': 'title',
    }
    
    
    
    
#  pip install django-elasticsearch-dsl django-elasticsearch-dsl-drf elasticsearch elasticsearch-dsl    



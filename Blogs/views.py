from rest_framework import viewsets
from django_elasticsearch_dsl_drf.filter_backends import (
    FilteringFilterBackend,
    CompoundSearchFilterBackend,
    OrderingFilterBackend,
)
from django_elasticsearch_dsl_drf.viewsets import DocumentViewSet
from .models import Category, Article
from .serializers import CategorySerializer, ArticleSerializer
from .documents import ArticleDocument

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ArticleViewSet(DocumentViewSet):
    document = ArticleDocument
    serializer_class = ArticleSerializer
    filter_backends = [
        FilteringFilterBackend,
        CompoundSearchFilterBackend,
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
    
    
    
   
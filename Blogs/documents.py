# package to index and search through articles, categories, and authors.
from django_elasticsearch_dsl import Document, fields
# registry of all the Document classes that will be used for indexing and searching.
from django_elasticsearch_dsl.registries import registry
from .models import Category, Article
from django.conf import settings
User = settings.AUTH_USER_MODEL


@registry.register_document
class CategoryDocument(Document):
    class Index:
        name = 'categories'
        settings = {
            'number_of_shards': 1, 
            'number_of_replicas': 0,
        }

    class Django:
        model = Category
        fields = [
            'name',
            'description',
        ]

@registry.register_document
class ArticleDocument(Document):
    class Index:
        name = 'articles'
        settings = {
            'number_of_shards': 1,
            'number_of_replicas': 0
        }

    category = fields.ObjectField(properties={
        'name': fields.TextField(),
        'description': fields.TextField(),
    })

    author = fields.ObjectField(properties={
        'username': fields.TextField(),
        'email': fields.TextField(),
    })

    class Django:
        model = Article
        fields = [
            'title',
            'content',
            'created_datetime',
            'updated_datetime',
        ]

        related_models = [Category, User]

        def get_queryset(self):
            return super().get_queryset().select_related(
                'category',
                'author'
            )
        



# @registry.register_document
# class ArticleDocument(Document):
#     # article_title = fields.TextField()
#     # content = fields.TextField()
#     # category = fields.ObjectField(properties={
#     #     'name': fields.TextField()
#     # })
#     # author = fields.ObjectField(properties={
#     #     'name': fields.TextField()
#     # })

#     class Index:
#         name = 'articles'
#         settings = {
#             'number_of_shards': 1,
#             'number_of_replicas': 0
#         }

#     class Django:
#         model = Article
#         fields = [
#             'id',
#             'title',
#             'content',
#             'category',
#         ]
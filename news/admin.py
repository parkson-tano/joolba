from django.contrib import admin
from .models import NewsModel, Comment, View

# Register your models here.
admin.site.register(NewsModel)
admin.site.register(Comment)

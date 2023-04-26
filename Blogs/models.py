from django.db import models
from django.conf import settings
User= settings.AUTH_USER_MODEL

class Category(models.Model):
    name = models.CharField(max_length=100)
    description=models.TextField(null=True, blank=True)
    
    def __str__(self):
        return self.name

class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_datetime = models.DateTimeField(auto_now_add=True)
    updated_datetime = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f'{self.author}: {self.title} ({self.created_datetime.date()})'


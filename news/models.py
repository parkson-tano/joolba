from django.db import models


# Create your models here.

class  NewsModel(models.Model):
    author = models.ForeignKey('settings.AUTH_USER_MODEL', on_delete=models.CASCADE)
    section = models.ForeignKey('sections.SectionModel', on_delete=models.CASCADE)
    category = models.ForeignKey('category.CategoryModel', on_delete=models.CASCADE)
    subcategory = models.ForeignKey('category.SubCategoryModel', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    headline = models.TextField()
    image = models.ImageField(upload_to='news')
    images = models.JSONField()
    content = models.TextField()
    view_count = models.IntegerField(default=0)
    deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

    def __str__(self):
        return self.title
    
class Image(models.Model):
    image = models.ImageField(upload_to='news')

    def __str__(self):
        return self.image.url
    
class Comment(models.Model):
    user = models.ForeignKey('settings.AUTH_USER_MODEL', on_delete=models.CASCADE)
    news = models.ForeignKey(NewsModel, on_delete=models.CASCADE)
    comment = models.TextField()
    deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.comment
    
class Like(models.Model):
    user = models.ForeignKey('settings.AUTH_USER_MODEL', on_delete=models.CASCADE)
    news = models.ForeignKey(NewsModel, on_delete=models.CASCADE)
    liked = models.BooleanField(default=False)
    deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username
    

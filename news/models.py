from django.db import models
from django.conf import settings
User = settings.AUTH_USER_MODEL

# Create your models here.

class  NewsModel(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    #subcategory = models.ForeignKey('sections.SubCategoryModel', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    headline = models.TextField()
    featured_image = models.ImageField(upload_to='news')
    other_image = models.ImageField(upload_to='news', blank = True)
    is_published = models.BooleanField(default = False)
    created_at = models.DateTimeField(auto_now_add=True)
    is_deleted = models.BooleanField(default=False)
    is_draft = models.BooleanField(default= False)
 
    

    def __str__(self):
        return self.title
    
    def view_count(self):
        return View.objects.filter(article=self).count()
  
    
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    article = models.ForeignKey(NewsModel, on_delete=models.CASCADE)
    comment = models.TextField()
    deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    liked = models.BooleanField( default= False)

    def __str__(self):
        return f'{self.user.username} on {self.article.title}'
    

class View(models.Model):
    article = models.ForeignKey(NewsModel, related_name = 'views', on_delete=models.CASCADE)
    view_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.article.title} on {self.view_date}'

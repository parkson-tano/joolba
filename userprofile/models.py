from django.db import models

# Create your models here.

class Viewed(models.Model):
    user = models.ForeignKey('authentications.User', on_delete=models.CASCADE)
    news = models.ForeignKey('news.NewsModel', on_delete=models.CASCADE)
    viewed = models.BooleanField(default=False)
    deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username
    
class Saved(models.Model):
    user = models.ForeignKey('authentications.User', on_delete=models.CASCADE)
    news = models.ForeignKey('news.NewsModel', on_delete=models.CASCADE)
    saved = models.BooleanField(default=False)
    deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username
    

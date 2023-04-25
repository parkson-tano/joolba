from rest_framework import serializers
from .models import NewsModel, Comment


class CommentsSerializer(serializers.ModelSerializer):
   
   class Meta:
        model = Comment
        fields = [
            'user',
            'article',
            'comment' ,
            'deleted',
            'created_at' ,
            
        ]

class NewsSerializer(serializers.ModelSerializer):
    featured_image = serializers.ImageField(max_length = None, use_url = True)
    other_image = serializers.ImageField(max_length = None, use_url = True)
    comments = CommentsSerializer(required=False, many=True)

    class Meta:
        model = NewsModel
        fields =[
                'id',
                'author', 
                #'subcategory',
                'title',
                'headline', 
                'content',
                'featured_image', 
                'other_image', 
                'is_published', 
                'created_at', 
                'is_draft', 
                'is_deleted', 
                'comments'
                
        ]
    


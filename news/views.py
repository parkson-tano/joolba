
from django.shortcuts import render
from .models import NewsModel, Comment
from .serializers import NewsSerializer, CommentsSerializer 
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response

# list of articles and creating new article.
class News(viewsets.ViewSet):
    #permission_classes = [permissions.IsAuthenticated]
    serializer_class = NewsSerializer

    def list(self, request):
        news = NewsModel.objects.all()
        serializer = self.serializer_class(news, many=True)
        return Response(serializer.data)
    
    
    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            is_draft = serializer.validated_data.get('is_draft')
            is_published = not is_draft if is_draft is not None else False  
            serializer.validated_data['is_published'] = is_published 
            article = serializer.save()  
            if not is_draft:  
                article.is_draft = False
                article.save()
            if is_draft:  
                draft_serializer = self.serializer_class(article)
            return Response(draft_serializer.data, status=201)
        else:  
                published_serializer = self.serializer_class(article)
                return Response(published_serializer.data, status=201)
        return Response(serializer.errors, status=400)


# Retrive, update, and delete single object 
class NewsDetail(viewsets.ViewSet):
    def get_news_object(self, pk):
        try:
            return NewsModel.objects.get(pk = pk)
        except NewsModel.DoesNotExist:
            return Response(status=404)
    
    def retrieve(self, request, pk=None):
        details = self.get_news_object(pk)
        serializer = NewsSerializer(details)
        return Response(serializer.data)

    def update(self, request, pk=None, *args, **kwargs):
        details = self.get_news_object(pk)
        if details is None:
            return Response({'error': 'Article not found'}, status = status.HTTP_404_NOT_FOUND)
        serializer = NewsSerializer(details, data = request.data)
        if serializer.is_valid():
            if details.author.id == request.user.id:
                serializer.save()
                return Response(serializer.data,status = status.HTTP_200_OK)
            return Response({"error": "You are not authorized to edit this article"},  status = 401)
        return Response(serializer.errors, status=400)


    def destroy(self, request, pk=None):
        details = self.get_news_object(pk)
        if details is None:
            return Response({'error': 'Article not found'}, status = status.HTTP_404_NOT_FOUND)
        if details.user.id == request.user.id:
            details.is_deleted = True
            details.is_published = False
            details.is_draft = False
            details.save()
            return Response(status=204)
        return Response({"error": "You are not authorized to delete this Article"}, status = status.HTTP_401_UNAUTHORIZED)
    

# post and retrieve all article related comments 
class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentsSerializer
    def get_object(self, pk):
        try:
            return  NewsModel.objects.get(pk = pk)
        except NewsModel.DoesNotExist:
            return None
        
    def get_queryset(self):
        news_article = self.get_object(self.kwargs['pk'])
        if news_article is None:
            return Comment.objects.none()
        return Comment.objects.filter(article=news_article)
    

    def list(self, request, pk= None):
        queryset = self.get_queryset()
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


    def post(self, request, pk, format=None):
        news_article = self.get_object(pk)
        data = {
            'user': request.user.id,
            'article': news_article.id,
            'comment': request.data.get('comment'),
            'deleted': request.data.get('deleted')
        }
        if news_article is None:
            return Response({'error': 'NEWS article not found'}, status = status.HTTP_400_BAD_REQUEST)
        serializer = CommentsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

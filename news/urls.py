from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static 
from .views import News, NewsDetail, CommentViewSet


urlpatterns = [
    path('news/', News.as_view({'get': 'list', 'put': 'create'}), name ='News'),
    path('news/<int:pk>/', NewsDetail.as_view({'get': 'retrieve', 'put':'update', 'delete': 'destroy'}), name = 'news-details'),
    path ('news/<int:pk>/comment/', CommentViewSet.as_view({'get': 'list'}), name = 'CommentViewSet') 
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('category/', include('category.urls')),
    # path('profile/', include('profiles.urls')),
    path('auth/', include('authentications.urls')),
    # path('news/', include('news.urls')),
    path('sections/', include('sections.urls')),
    # path('userprofile/', include('userprofile.urls')),
    
    # for doc ui
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),    
    path('', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/docs/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),

]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

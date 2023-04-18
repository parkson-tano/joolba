from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('category/', include('category.urls')),
    # path('profile/', include('profiles.urls')),
    path('auth/', include('authentications.urls')),
    # path('news/', include('news.urls')),
    # path('sections/', include('sections.urls')),
    # path('userprofile/', include('userprofile.urls')),
    path('blog/', include('Blogs.urls')),
    path('admin/', admin.site.urls),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

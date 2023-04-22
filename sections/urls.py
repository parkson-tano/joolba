from . import views
from django.urls import path, include
from rest_framework_nested import routers


router = routers.DefaultRouter()
router.register(
    "sectionmodels", views.SectionModelViewSet, basename="sectionmodels"
)
router.register(
    "categorymodels", views.CategoryModelViewSet, basename="categorymodels"
)

urlpatterns = [
    path("", include(router.urls)),
]

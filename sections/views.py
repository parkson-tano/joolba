from .models import *
from .serializers import *
from rest_framework import viewsets, permissions, response
from drf_spectacular.utils import extend_schema

class SectionModelViewSet(viewsets.ModelViewSet):
    http_method_names = ["get"]
    queryset = SectionModel.objects.filter(deleted=False).prefetch_related(
        "categorymodel_set"
    )
    serializer_class = SectionModelSerializer
    permission_classes = []


class CategoryModelViewSet(viewsets.ModelViewSet):
    http_method_names = ["get"]
    queryset = CategoryModel.objects.filter(deleted=False).prefetch_related(
        "subcategorymodel_set"
    )
    # serializer_class = CategoryModelSerializer
    permission_classes = []

    @extend_schema(
    tags=["categorymodel"],
    request=CategoryModelSerializer,
    responses={200: CategoryModelSerializer},
    methods=["GET"], 
    description= "Joolba Category Model"
    )
    def list(self, request):
        serializer = CategoryModelSerializer(self.queryset, many=True)
        return response.Response(serializer.data)

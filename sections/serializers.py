from .models import *
from rest_framework import serializers


class SectionModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = SectionModel
        fields = "__all__"


class SubCategoryModelSeriaizer(serializers.ModelSerializer):
    class Meta:
        model = SubCategoryModel
        fields = ["id", "name", "deleted"]


class CategoryModelSerializer(serializers.ModelSerializer):
    subcategories = serializers.SerializerMethodField()

    class Meta:
        model = CategoryModel
        fields = ["id", "name", "deleted","section","subcategories"]

    def to_representation(self, instance):
        self.fields["section"] = serializers.StringRelatedField()
        return super().to_representation(instance)

    def get_subcategories(self, obj):
        return obj.subcategorymodel_set.filter(category_id=obj.id).values(
            "id", "name", "deleted"
        )

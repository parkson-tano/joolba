from .models import *
from django.contrib import admin


class BaseSectionAppAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "deleted", "created_at", "updated_at"]
    date_hierarchy = "created_at"
    list_filter = ["deleted"]
    list_display_links = ["id", "name"]
    list_per_page = 25


@admin.register(SectionModel)
class SectionModelAdmin(BaseSectionAppAdmin):
    pass


@admin.register(CategoryModel)
class CategoryModelAdmin(BaseSectionAppAdmin):
    list_display = [
        "id",
        "section",
        "name",
        "deleted",
        "created_at",
        "updated_at",
    ]


@admin.register(SubCategoryModel)
class SubCategoryModelAdmin(BaseSectionAppAdmin):
    pass

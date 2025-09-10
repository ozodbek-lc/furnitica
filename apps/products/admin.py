from django.contrib import admin
from .models import CatalogModel, CategoryModel, ColorModel, TagModel, ProductModel


@admin.register(CatalogModel)
class CatalogAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at']
    search_fields = ['title']


@admin.register(CategoryModel)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at']
    search_fields = ['title']


@admin.register(ColorModel)
class ColorAdmin(admin.ModelAdmin):
    list_display = ['title', 'color', 'created_at']
    search_fields = ['title']


@admin.register(TagModel)
class TagAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at']
    search_fields = ['title']


@admin.register(ProductModel)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'category', 'catalog', 'created_at']
    list_filter = ['category', 'catalog', 'colors', 'tags', 'created_at']
    search_fields = ['title', 'description']
    filter_horizontal = ['colors', 'tags']

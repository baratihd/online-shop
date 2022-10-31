from django.contrib import admin

from .models import CategoryModel, ProductModel


@admin.register(CategoryModel)
class CategoryModelAdmin(admin.ModelAdmin):
    search_fields = ('title',)


@admin.register(ProductModel)
class ProductModelAdmin(admin.ModelAdmin):
    search_fields = ('title', 'reference_number')

from django.contrib import admin
from .models import Product, ProductImage, Category

class ProductImageInline(admin.TabularInline):
    """ Inline admin for product images """
    model = ProductImage
    fields = ['thumbnail_image', 'detailed_image']
    extra = 0


class ProductAdmin(admin.ModelAdmin):
    """ Admin for products """
    list_display = ('sku', 'name', 'category', 'price',  'card_type', 'rating')
    ordering = ('sku',)
    inlines = [ProductImageInline]
    search_fields = ('sku', 'name', 'description', 'category__name')
    list_filter = ('category', 'card_type', 'rating')


class CategoryAdmin(admin.ModelAdmin):
    """ Admin for categories """
    list_display = ('friendly_name', 'name')
    search_fields = ('name', 'friendly_name')

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
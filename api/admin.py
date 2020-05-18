from django.contrib import admin
from api.models import (
    SwitchTypesModel, ProductImageModel, 
    ProductModel, ProductReviewModel,
    BrandsModel, SlidshowProductsModel
)

admin.site.site_header = "KeyBrasil"
admin.site.site_title = "KeyBrasil"
admin.site.index_title = "Administration"

# Register your models here.
@admin.register(BrandsModel)
class BrandsAdmin (admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    search_fields = ('name',)
    list_filter = ('name',)
    list_display = ('preview', 'id', 'name', 'slug','updated_at', 'created_at')

# Register your models here.
@admin.register(SwitchTypesModel)
class SwitchTypesAdmin (admin.ModelAdmin):
    filter_horizontal = ('images', )
    prepopulated_fields = {"slug": ("name",)}
    search_fields = ('name', 'model_name')
    list_filter = ('name','model_name')
    list_display = ('preview', 'name', 'model_name', 'slug','updated_at', 'created_at')

@admin.register(ProductImageModel)
class ProductImageAdmin (admin.ModelAdmin):
    search_fields = ('name', 'url')
    list_display = ('preview', 'name', 'updated_at', 'created_at')

@admin.register(ProductReviewModel)
class ProductReviewAdmin (admin.ModelAdmin):
    search_fields = ('author_name', 'author_email')
    list_display = ('author_name', 'author_email', 'review_rating','updated_at', 'created_at')

@admin.register(ProductModel)
class ProductAdmin (admin.ModelAdmin):
    filter_horizontal = ('images', 'switch_type')
    prepopulated_fields = {"slug": ("name",)}
    search_fields = ('model_name',)
    list_filter = ('brand_fk', 'price')
    list_display = ('preview', 'brand_fk','name', 'slug', 'price', 'stock_count')


@admin.register(SlidshowProductsModel)
class SlideshowAdmin (admin.ModelAdmin):
    list_display = ('name',)
    filter_horizontal = ('products',)
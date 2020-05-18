from django.contrib.auth.models import User, Group
from rest_framework import serializers

from api.models import (
    ProductImageModel, ProductModel, 
    ProductReviewModel, SwitchTypesModel,
    BrandsModel, SlidshowProductsModel
)

class BrandsSerializer (serializers.ModelSerializer):
    class Meta:
        model = BrandsModel
        fields = ['slug', 'name', 'text', 'image']

class ProductImageSerializer (serializers.ModelSerializer):
    class Meta:
        model = ProductImageModel
        fields = ['name', 'url']

class SwitchTypesSerializer (serializers.HyperlinkedModelSerializer):
    images = ProductImageSerializer(read_only=True, many=True)

    class Meta:
        model = SwitchTypesModel
        fields = ['name', 'model_name', 'slug', 'images']

class ProductSerializer (serializers.HyperlinkedModelSerializer):
    images = ProductImageSerializer(read_only=True, many=True)
    switch_type = SwitchTypesSerializer(read_only=True, many=True)
    star_value = serializers.SerializerMethodField(method_name='bleh')

    class Meta:
        model = ProductModel
        fields = ['id', 'name', 'model_name', 'slug','price', 'stock_count', 'star_value', 'switch_type','images']

    def bleh (self, obj):
        return 4

class ProductReviewSerializer (serializers.ModelSerializer):
    class Meta:
        model = ProductReviewModel
        fields = ['product_fk', 'author_name', 'author_email', 'review_text', 'review_rating']

class SlidshowProductsSerializer (serializers.ModelSerializer):
    products = ProductSerializer(read_only=True, many=True)

    class Meta:
        model = SlidshowProductsModel
        fields = ['name', 'products']

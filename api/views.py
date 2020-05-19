from django.contrib.auth.models import User, Group
from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
import json

from api.serializers import (
    SwitchTypesSerializer, ProductImageSerializer, 
    ProductReviewSerializer, ProductSerializer,
    BrandsSerializer, SlidshowProductsSerializer
)

from api.models import (
    ProductImageModel, ProductModel,
    ProductReviewModel, SwitchTypesModel,
    BrandsModel, SlidshowProductsModel
)

class BrandsViewSet(viewsets.ModelViewSet):
    queryset = BrandsModel.objects.all()
    serializer_class = BrandsSerializer

class SwitchTypesViewSet(viewsets.ModelViewSet):
    queryset = SwitchTypesModel.objects.all()
    serializer_class = SwitchTypesSerializer

class ProductImageViewSet(viewsets.ModelViewSet):
    queryset = ProductImageModel.objects.all()
    serializer_class = ProductImageSerializer

class ProductReviewViewSet(viewsets.ModelViewSet):
    queryset = ProductReviewModel.objects.all()
    serializer_class = ProductReviewSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = ProductModel.objects.all()
    serializer_class = ProductSerializer

class SlidshowViewSet(APIView):
    def get(self, request):
        slide = SlidshowProductsModel.objects.order_by("-created_at")[0]
        results = {
            'id': slide.id,
            'name': slide.name,
            'products' : [{
                    'id' : p.id,
                    'model' : p.model_name,
                    'name' : p.name,
                    'brand' : p.brand_fk.name,
                    'stars' : p.star_value,
                    'slug' : p.slug,
                    'price' : p.price,
                    'main_image' : p.images.all()[0].url
                } for p in slide.products.all()
            ],
            'created_at' : slide.created_at,
            'updated_at' : slide.updated_at
        }

        data = {
            'count': 1,
            'filter' : 'recent',
            'results': results
        }

        return Response(data)
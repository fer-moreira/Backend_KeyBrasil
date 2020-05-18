from django.contrib.auth.models import User, Group
from rest_framework import viewsets, permissions
from rest_framework.response import Response

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

class SlidshowViewSet(viewsets.ModelViewSet):
    queryset = SlidshowProductsModel.objects.all()
    serializer_class = SlidshowProductsSerializer
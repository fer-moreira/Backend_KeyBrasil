from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import RedirectView
from rest_framework import routers

from api.views import (
    ProductImageViewSet, ProductReviewViewSet, 
    ProductViewSet, SwitchTypesViewSet,
    BrandsViewSet, SlidshowViewSet
)

router = routers.DefaultRouter()

router.register('images', ProductImageViewSet)
router.register('review', ProductReviewViewSet)
router.register('product', ProductViewSet)
router.register('switch', SwitchTypesViewSet)
router.register('brands', BrandsViewSet)
router.register('slidshow', SlidshowViewSet)

urlpatterns = [
    path('store/', include(router.urls)),
    path('auth/', include('rest_framework.urls', namespace='rest_framework'))
]
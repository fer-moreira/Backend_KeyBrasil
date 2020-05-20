from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import RedirectView
from rest_framework import routers

from api.views import (
    ProductImageViewSet, ProductReviewViewSet, 
    ProductViewSet, SwitchTypesViewSet,
    BrandsViewSet, SlidshowViewSet, ItemsGridViewSet
)

router = routers.DefaultRouter()

router.register('images', ProductImageViewSet)
router.register('review', ProductReviewViewSet)
router.register('product', ProductViewSet)
router.register('switch', SwitchTypesViewSet)
router.register('brands', BrandsViewSet)

urlpatterns = [
    path('store/', include(router.urls)),
    path('auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('store/slideshow/', SlidshowViewSet.as_view()),
    path('store/itemsgrid/', ItemsGridViewSet.as_view()),
]
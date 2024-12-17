from django.urls import path, include
from rest_framework import routers

from . import api

router = routers.DefaultRouter()
router.register('Brand', api.BrandViewSet)
router.register('Material', api.MaterialViewSet)
router.register('Size', api.SizeViewSet)
router.register('Color', api.ColorViewSet)

urlpatterns = (
    path('', include(router.urls)),
    path('categories/', api.CategoryListAPIView.as_view()),
    path('category/<int:pk>/', api.CategoryRetrieveAPIView.as_view()),

    path('product/<int:pk>', api.ProductRetrieveAPIView.as_view()),
    path('productvariant/<int:pk>', api.ProductVariantRetrieveAPIView.as_view()),
    path('productVariants/', api.ProductVariantListAPIView.as_view()),
)

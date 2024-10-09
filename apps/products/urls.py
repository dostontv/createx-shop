from django.urls import path, include
from rest_framework import routers

from . import api

router = routers.DefaultRouter()
router.register("Category", api.CategoryViewSet)
router.register("Color", api.ColorViewSet)
router.register("Product", api.ProductViewSet)
router.register("ProductVariant", api.ProductVariantViewSet)
# router.register("Size", api.SizeViewSet)

urlpatterns = (
    path("", include(router.urls)),

)

from django.urls import path, include
from rest_framework import routers

from . import api

router = routers.DefaultRouter()
router.register('Category', api.CategoryViewSet)

urlpatterns = (
    path('', include(router.urls)),
    path('product/<int:pk>', api.ProductVariantRetrieveAPIView.as_view()),
    path('products/', api.ProductListAPIView.as_view()),
)


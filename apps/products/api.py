from drf_spectacular.utils import extend_schema
from rest_framework import viewsets, permissions
from rest_framework.generics import ListAPIView, RetrieveAPIView
from django.db.models import Count

from . import filters
from . import models
from . import serializers
from .pagination import CustomCursorPagination


@extend_schema(tags=['Categories'])
class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    """ViewSet for the Category class"""

    queryset = models.Category.objects.annotate(product_count=Count('products'))
    serializer_class = serializers.CategoryDetailSerializer
    permission_classes = [permissions.AllowAny]


@extend_schema(tags=['Colors'])
class ColorViewSet(viewsets.ReadOnlyModelViewSet):
    """ViewSet for the Color class"""

    queryset = models.Color.objects.all()
    serializer_class = serializers.ColorSerializer
    permission_classes = [permissions.IsAuthenticated]


@extend_schema(tags=['Products'])
class ProductListAPIView(ListAPIView):
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer
    filterset_class = filters.ProductFilter
    pagination_class = CustomCursorPagination


@extend_schema(tags=['Products'])
class ProductRetrieveAPIView(RetrieveAPIView):
    """ViewSet for the ProductVariant class"""

    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductRetrieveSerializer

    def get(self, request, *args, **kwargs):
        product = self.get_object()
        if product:
            product.views += 1
            product.save()

        return super().get(request, *args, **kwargs)


@extend_schema(tags=['Products'])
class ProductVariantRetrieveAPIView(RetrieveAPIView):
    """ViewSet for the ProductVariant class"""

    queryset = models.ProductVariant.objects.all()
    serializer_class = serializers.ProductVariantSerializer


@extend_schema(tags=['Size'])
class SizeViewSet(viewsets.ReadOnlyModelViewSet):
    """ViewSet for the Size class"""

    queryset = models.Size.objects.all()
    serializer_class = serializers.SizeSerializer
    permission_classes = [permissions.IsAuthenticated]

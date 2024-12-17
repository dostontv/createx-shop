from django.db.models import Count
from drf_spectacular.utils import extend_schema
from rest_framework import viewsets, permissions
from rest_framework.generics import ListAPIView, RetrieveAPIView

from . import filters
from . import models
from . import serializers
from .pagination import CustomCursorPagination


@extend_schema(tags=['Categories'])
class CategoryListAPIView(ListAPIView):
    queryset = models.Category.objects.filter(parent=None)
    serializer_class = serializers.CategoryListSerializer


@extend_schema(tags=['Categories'])
class CategoryRetrieveAPIView(RetrieveAPIView):
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategoryRetrieveSerializer


@extend_schema(tags=['Colors'])
class ColorViewSet(viewsets.ReadOnlyModelViewSet):
    """ViewSet for the Color class"""

    queryset = models.Color.objects.all()
    serializer_class = serializers.ColorSerializer
    permission_classes = [permissions.IsAuthenticated]


@extend_schema(tags=['Colors'])
class BrandViewSet(viewsets.ReadOnlyModelViewSet):
    """ViewSet for the Brand class"""

    queryset = models.Brand.objects.all()
    serializer_class = serializers.BrandSerializer
    permission_classes = [permissions.AllowAny]


@extend_schema(tags=['Colors'])
class MaterialViewSet(viewsets.ReadOnlyModelViewSet):
    """ViewSet for the Material class"""

    queryset = models.Material.objects.all()
    serializer_class = serializers.MaterialSerializer
    permission_classes = [permissions.AllowAny]


@extend_schema(tags=['Products'])
class ProductRetrieveAPIView(RetrieveAPIView):
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductRetrieveSerializer


@extend_schema(tags=['Products'])
class ProductVariantListAPIView(ListAPIView):
    queryset = models.ProductVariant.objects.all()
    serializer_class = serializers.ProductVariantListSerializer
    # filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_class = filters.ProductFilter
    pagination_class = CustomCursorPagination
    ordering_fields = ['views', 'created']
    ordering = ['created']


@extend_schema(tags=['Products'])
class ProductVariantRetrieveAPIView(RetrieveAPIView):
    queryset = models.ProductVariant.objects.all()
    serializer_class = serializers.ProductVariantSerializer

    def get(self, request, *args, **kwargs):
        product_variant = self.get_object()
        if product_variant:
            product_variant.views += 1
            product_variant.save()
        return super().get(request, *args, **kwargs)


@extend_schema(tags=['Size'])
class SizeViewSet(viewsets.ReadOnlyModelViewSet):
    """ViewSet for the Size class"""

    queryset = models.Size.objects.all()
    serializer_class = serializers.SizeSerializer
    permission_classes = [permissions.IsAuthenticated]

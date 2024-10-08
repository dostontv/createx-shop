from rest_framework import viewsets, permissions

from . import serializers
from . import models


class CategoryViewSet(viewsets.ModelViewSet):
    """ViewSet for the Category class"""

    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer
    permission_classes = [permissions.IsAuthenticated]


class ColorViewSet(viewsets.ModelViewSet):
    """ViewSet for the Color class"""

    queryset = models.Color.objects.all()
    serializer_class = serializers.ColorSerializer
    permission_classes = [permissions.IsAuthenticated]


class ProductViewSet(viewsets.ModelViewSet):
    """ViewSet for the Product class"""

    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer
    permission_classes = [permissions.IsAuthenticated]


class ProductVariantViewSet(viewsets.ModelViewSet):
    """ViewSet for the ProductVariant class"""

    queryset = models.ProductVariant.objects.all()
    serializer_class = serializers.ProductVariantSerializer
    permission_classes = [permissions.IsAuthenticated]


class SizeViewSet(viewsets.ModelViewSet):
    """ViewSet for the Size class"""

    queryset = models.Size.objects.all()
    serializer_class = serializers.SizeSerializer
    permission_classes = [permissions.IsAuthenticated]

from rest_framework import serializers

from . import models


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Category
        fields = [
            "parent",
            "last_updated",
            "created",
            "name",
        ]

class ColorSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Color
        fields = [
            "name",
            "last_updated",
            "created",
        ]

class ContentSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Content
        fields = [
            "last_updated",
            "content",
            "created",
            "product_variant",
        ]

class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Product
        fields = [
            "description",
            "last_updated",
            "name",
            "category",
            "created",
        ]

class ProductVariantSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.ProductVariant
        fields = [
            "quantity",
            "color",
            "price",
            "product",
            "last_updated",
            "size",
            "created",
        ]

class SizeSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Size
        fields = [
            "name",
            "last_updated",
            "created",
        ]

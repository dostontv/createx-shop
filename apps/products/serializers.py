from rest_framework import serializers

from . import models


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = [
            "id",
            "name",
            "created",
            "last_updated",
        ]


class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Color
        fields = [
            "id",
            "name",
            "created",
            "last_updated",
        ]


class ContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Content
        fields = [
            "id",
            "content",
            "created",
            "product_variant",
            "last_updated",
        ]


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Product
        fields = [
            "id",
            "name",
            "description",
            "category",
            "views",
            "created",
            "last_updated",
        ]

    def to_representation(self, instance):
        data = super().to_representation(instance)

        data['category'] = CategorySerializer(instance.category).data
        return data


class ProductVariantSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ProductVariant
        fields = [
            "quantity",
            "price",
            "product",
            "color",
            "size",
            "created",
            "last_updated",
        ]


class SizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Size
        fields = [
            "name",
            "last_updated",
            "created",
        ]

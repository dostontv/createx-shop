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
        variants = list(instance.variants.all())
        i = 0
        while i < len(variants):
            variants[i] = ProductVariantSerializer(variants[i]).data
            i += 1

        data['variants'] = variants
        return data


class CategoryDetailSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True)
    product_count = serializers.IntegerField()

    class Meta:
        model = models.Category
        fields = ['id', 'name', 'products', 'product_count']


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

    def to_representation(self, instance):
        data = super().to_representation(instance)
        content = []
        for con in instance.content.all():
            content.append({"url": con.content.url})
        return data


class SizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Size
        fields = [
            "name",
            "last_updated",
            "created",
        ]

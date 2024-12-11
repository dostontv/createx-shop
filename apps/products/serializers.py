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


class ProductRetrieveSerializer(serializers.ModelSerializer):
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


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Product
        fields = [
            "id",
            "name",
            "views",
        ]


class ProductVariantListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ProductVariant
        fields = [
            "id",
            "price",
        ]

    def to_representation(self, instance):
        data = super().to_representation(instance)
        content = []
        for con in instance.content.all():
            content_url = con.content.url
            i = 0
            if (j := content_url.find('https')) >= 0:
                i = j
            content.append({"url": content_url[i:]})
        data['content'] = content
        data['product'] = ProductSerializer(instance.product).data
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
            "brand",
            "material",
            "created",
        ]

    def to_representation(self, instance):
        data = super().to_representation(instance)
        content = []
        for con in instance.content.all():
            content_url = con.content.url
            i = 0
            if (j := content_url.find('https')) >= 0:
                i = j
            content.append({"url": content_url[i:]})

        data['content'] = content
        data['color'] = {"id": instance.color.id, "name": instance.color.name}
        if hasattr(instance, "size") and hasattr(instance.size, "id"):
            data['size'] = {"id": instance.size.id, "name": instance.size.name}
        data['product'] = ProductSerializer(instance.product).data
        if hasattr(instance, "brand") and hasattr(instance.brand, "id"):
            data['brand'] = {"id": instance.brand.id, "name": instance.brand.name}
        if hasattr(instance, "material") and hasattr(instance.material, "id"):
            data['material'] = {"id": instance.material.id, "name": instance.material.name}

        return data


class SizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Size
        fields = [
            'id',
            "name",
            "last_updated",
            "created",
        ]

from rest_framework import serializers

from . import models


class CartSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Cart
        fields = [
            "product_variant",
            "user",
            "created",
        ]

class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Order
        fields = [
            "user",
            "last_updated",
            "created",
        ]

class OrderItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.OrderItem
        fields = [
            "order",
            "product_variant",
        ]

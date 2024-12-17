from rest_framework import serializers
from . import models


# Cart Serializers

class CartCreateSerializer(serializers.ModelSerializer):
    """Serializer for creating a cart."""

    class Meta:
        model = models.Cart
        fields = [
            "product_variant",
            "quantity",
        ]

    def save(self, **kwargs):
        return super().save(**kwargs)


class CartUpdateSerializer(serializers.ModelSerializer):
    """Serializer for updating a cart."""

    class Meta:
        model = models.Cart
        fields = [
            "product_variant",
            "quantity",  # Allow quantity updates
        ]


class CartRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Cart
        fields = [
            "product_variant",
            "quantity",
            "created",
        ]


class CartListSerializer(serializers.ModelSerializer):
    """Serializer for listing carts."""

    class Meta:
        model = models.Cart
        fields = ['id', 'product_variant', 'quantity', 'created']


# Order Serializers
class OrderListSerializer(serializers.ModelSerializer):
    """Serializer for listing orders."""

    class Meta:
        model = models.Order
        fields = ['uid', 'status', 'txn_status', 'created', 'user']


class OrderCreateSerializer(serializers.ModelSerializer):
    """Serializer for creating an order."""

    class Meta:
        model = models.Order
        fields = [
            "status",
            "txn_status",
        ]


class OrderUpdateSerializer(serializers.ModelSerializer):
    """Serializer for updating an order."""

    class Meta:
        model = models.Order
        fields = [
            "status",  # Only status can be updated
            "txn_status",
        ]


class OrderRetrieveSerializer(serializers.ModelSerializer):
    """Serializer for retrieving order details."""

    class Meta:
        model = models.Order
        fields = [
            "uid",
            "status",
            "txn_status",
            "created",
            "last_updated",
        ]


# OrderItem Serializers
class OrderItemListSerializer(serializers.ModelSerializer):
    """Serializer for listing order items."""

    class Meta:
        model = models.OrderItem
        fields = ['order', 'product_variant', 'quantity']


class OrderItemCreateSerializer(serializers.ModelSerializer):
    """Serializer for creating an order item."""

    class Meta:
        model = models.OrderItem
        fields = [
            "order",
            "product_variant",
            "quantity",  # Allow quantity to be set during creation
        ]


class OrderItemUpdateSerializer(serializers.ModelSerializer):
    """Serializer for updating an order item."""

    class Meta:
        model = models.OrderItem
        fields = [
            "product_variant",
            "quantity",  # Allow quantity updates
        ]


class OrderItemRetrieveSerializer(serializers.ModelSerializer):
    """Serializer for retrieving order item details."""

    class Meta:
        model = models.OrderItem
        fields = [
            "order",
            "product_variant",
            "quantity",  # Include quantity during retrieval
        ]

from rest_framework import serializers
from . import models
from ..products.models import ProductVariant
from ..products.serializers import ProductVariantListSerializer


# Cart Serializers

class CartCreateSerializer(serializers.ModelSerializer):
    """Serializer for creating a cart."""

    class Meta:
        model = models.Cart
        fields = [
            "product_variant",
            "quantity",
        ]

    def validate(self, attrs):
        quantity = attrs["quantity"]
        product = attrs["product_variant"]
        product_variant = ProductVariant.objects.get(pk=product.id)
        if product_variant.quantity < quantity:
            raise serializers.ValidationError('Not enough quantity')
        return super().validate(attrs)

    def create(self, validated_data):
        user = validated_data['user']
        product = validated_data['product_variant']
        Cart = models.Cart.objects.filter(user=user, product_variant=product)
        if Cart.exists():
            Cart = Cart.first()
            Cart.quantity += validated_data['quantity']
            Cart.save()
            return Cart
        return super().create(validated_data)


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
        fields = ['uid', 'status', 'txn_status', 'created']

    def to_representation(self, instance):
        data = super().to_representation(instance)
        orderitems = models.OrderItem.objects.filter(order_id=data['uid'])
        data['products'] = []
        for product in orderitems:
            data['products'].append(OrderItemListSerializer(product).data)
        return data


class OrderCreateSerializer(serializers.ModelSerializer):
    """Serializer for creating an order."""

    class Meta:
        model = models.Order
        fields = ['uid']
        extra_kwargs = {
            'uid': {'read_only': True},
        }

    def create(self, validated_data):
        user = validated_data['user']
        if not user.carts.all().exists():
            raise serializers.ValidationError('Not enough cart')
        Order = models.Order.objects.create(user=user)
        for cart in user.carts.all():
            models.OrderItem.objects.create(order=Order, product_variant=cart.product_variant, quantity=cart.quantity)
            cart.delete()
        return Order


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

    def to_representation(self, instance):
        data = super().to_representation(instance)
        product_variant = data.pop('product_variant')
        data['product_variant'] = ProductVariantListSerializer(ProductVariant.objects.get(pk=product_variant)).data
        return data


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

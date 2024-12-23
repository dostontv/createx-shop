from drf_spectacular.utils import extend_schema
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from . import models
from . import serializers


# Cart Views
@extend_schema(tags=['Cart'])
class CartCreateView(generics.CreateAPIView):
    queryset = models.Cart.objects.all()
    serializer_class = serializers.CartCreateSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = super().get_queryset().filter(user=self.request.user)
        return queryset

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


@extend_schema(tags=['Cart'])
class CartListView(generics.ListAPIView):
    queryset = models.Cart.objects.all()
    serializer_class = serializers.CartListSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = super().get_queryset().filter(user=self.request.user)
        return queryset


@extend_schema(tags=['Cart'])
class CartRetrieveView(generics.RetrieveAPIView):
    queryset = models.Cart.objects.all()
    serializer_class = serializers.CartRetrieveSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = super().get_queryset().filter(user=self.request.user)
        return queryset


@extend_schema(tags=['Cart'])
class CartUpdateView(generics.UpdateAPIView):
    # check user's Cart
    queryset = models.Cart.objects.all()
    serializer_class = serializers.CartUpdateSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = super().get_queryset().filter(user=self.request.user)
        return queryset


@extend_schema(tags=['Cart'])
class CartDeleteView(generics.DestroyAPIView):
    # check user's Cart
    queryset = models.Cart.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = serializers.CartListSerializer

    def get_queryset(self):
        queryset = super().get_queryset().filter(user=self.request.user)
        return queryset


# Order Views
@extend_schema(tags=['Order'])
class OrderCreateView(generics.CreateAPIView):
    """Create a new order."""
    queryset = models.Order.objects.all()
    serializer_class = serializers.OrderCreateSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = super().get_queryset().filter(user=self.request.user)
        return queryset

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


@extend_schema(tags=['Order'])
class OrderListView(generics.ListAPIView):
    """List all orders."""
    queryset = models.Order.objects.all()
    serializer_class = serializers.OrderListSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = super().get_queryset().filter(user=self.request.user)
        return queryset


@extend_schema(tags=['Order'])
class OrderRetrieveView(generics.RetrieveAPIView):
    """Retrieve a specific order."""
    queryset = models.Order.objects.all()
    serializer_class = serializers.OrderRetrieveSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = super().get_queryset().filter(user=self.request.user)
        return queryset


@extend_schema(tags=['Order'])
class OrderUpdateView(generics.UpdateAPIView):
    """Update an existing order."""
    queryset = models.Order.objects.all()
    serializer_class = serializers.OrderUpdateSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = super().get_queryset().filter(user=self.request.user)
        return queryset


@extend_schema(tags=['Order'])
class OrderDeleteView(generics.DestroyAPIView):
    """Delete an order."""
    queryset = models.Order.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = serializers.OrderListSerializer

    def get_queryset(self):
        queryset = super().get_queryset().filter(user=self.request.user)
        return queryset


# OrderItem Views
# @extend_schema(tags=['OrderItem'])
# class OrderItemCreateView(generics.CreateAPIView):
#     """Create a new order item."""
#     queryset = models.OrderItem.objects.all()
#     serializer_class = serializers.OrderItemCreateSerializer
#     permission_classes = [IsAuthenticated]
#
#     def get_queryset(self):
#         queryset = super().get_queryset().filter(user=self.request.user)
#         return queryset
#
#
# @extend_schema(tags=['OrderItem'])
# class OrderItemListView(generics.ListAPIView):
#     """List all order items."""
#     queryset = models.OrderItem.objects.all()
#     serializer_class = serializers.OrderItemListSerializer
#     permission_classes = [IsAuthenticated]
#
#     def get_queryset(self):
#         queryset = super().get_queryset().filter(user=self.request.user)
#         return queryset
#
#
# @extend_schema(tags=['OrderItem'])
# class OrderItemRetrieveView(generics.RetrieveAPIView):
#     """Retrieve a specific order item."""
#     queryset = models.OrderItem.objects.all()
#     serializer_class = serializers.OrderItemRetrieveSerializer
#     permission_classes = [IsAuthenticated]
#
#     def get_queryset(self):
#         queryset = super().get_queryset().filter(user=self.request.user)
#         return queryset
#
#
# @extend_schema(tags=['OrderItem'])
# class OrderItemUpdateView(generics.UpdateAPIView):
#     """Update an existing order item."""
#     queryset = models.OrderItem.objects.all()
#     serializer_class = serializers.OrderItemUpdateSerializer
#     permission_classes = [IsAuthenticated]
#
#     def get_queryset(self):
#         queryset = super().get_queryset().filter(user=self.request.user)
#         return queryset
#
#
# @extend_schema(tags=['OrderItem'])
# class OrderItemDeleteView(generics.DestroyAPIView):
#     """Delete an order item."""
#     queryset = models.OrderItem.objects.all()
#     serializer_class = serializers.OrderItemListSerializer
#     permission_classes = [IsAuthenticated]
#
#     def get_queryset(self):
#         queryset = super().get_queryset().filter(user=self.request.user)
#         return queryset

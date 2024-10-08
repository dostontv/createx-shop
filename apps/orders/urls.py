from django.urls import path, include
from rest_framework import routers

from . import api

router = routers.DefaultRouter()
router.register("Cart", api.CartViewSet)
router.register("Order", api.OrderViewSet)
router.register("OrderItem", api.OrderItemViewSet)

urlpatterns = (
    path("", include(router.urls)),
)

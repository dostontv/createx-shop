from django.urls import path

from apps.orders.api import CartCreateView, CartListView, CartRetrieveView, CartUpdateView, CartDeleteView, \
    OrderCreateView, OrderListView, OrderRetrieveView, OrderUpdateView, OrderDeleteView
# OrderItemCreateView, \
#     OrderItemListView, OrderItemRetrieveView, OrderItemUpdateView, OrderItemDeleteView

urlpatterns = [
    # Cart URLs
    path('cart/', CartCreateView.as_view(), name='cart-create'),
    path('cart/list/', CartListView.as_view(), name='cart-list'),
    path('cart/<int:pk>/', CartRetrieveView.as_view(), name='cart-retrieve'),
    path('cart/update/<int:pk>/', CartUpdateView.as_view(), name='cart-update'),
    path('cart/delete/<int:pk>/', CartDeleteView.as_view(), name='cart-delete'),

    # Order URLs
    path('order/', OrderCreateView.as_view(), name='order-create'),
    path('order/list/', OrderListView.as_view(), name='order-list'),
    path('order/<str:pk>/', OrderRetrieveView.as_view(), name='order-retrieve'),
    path('order/update/<str:pk>/', OrderUpdateView.as_view(), name='order-update'),
    path('order/delete/<str:pk>/', OrderDeleteView.as_view(), name='order-delete'),

    # OrderItem URLs
    # path('order-item/', OrderItemCreateView.as_view(), name='order-item-create'),
    # path('order-item/list/', OrderItemListView.as_view(), name='order-item-list'),
    # path('order-item/<int:pk>/', OrderItemRetrieveView.as_view(), name='order-item-retrieve'),
    # path('order-item/update/<int:pk>/', OrderItemUpdateView.as_view(), name='order-item-update'),
    # path('order-item/delete/<int:pk>/', OrderItemDeleteView.as_view(), name='order-item-delete'),
]

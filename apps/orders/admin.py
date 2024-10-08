from django.contrib import admin
from django import forms

from . import models


class CartAdminForm(forms.ModelForm):

    class Meta:
        model = models.Cart
        fields = "__all__"


class CartAdmin(admin.ModelAdmin):
    form = CartAdminForm
    list_display = [
        "user",
        "created",
    ]


class OrderAdminForm(forms.ModelForm):

    class Meta:
        model = models.Order
        fields = "__all__"


class OrderAdmin(admin.ModelAdmin):
    form = OrderAdminForm
    list_display = [
        "user",
        "last_updated",
        "created",
    ]


class OrderItemAdminForm(forms.ModelForm):

    class Meta:
        model = models.OrderItem
        fields = "__all__"


class OrderItemAdmin(admin.ModelAdmin):
    form = OrderItemAdminForm
    list_display = [
        "order",
    ]


admin.site.register(models.Cart, CartAdmin)
admin.site.register(models.Order, OrderAdmin)
admin.site.register(models.OrderItem, OrderItemAdmin)

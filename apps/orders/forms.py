from django import forms
from . import models


class CartForm(forms.ModelForm):
    class Meta:
        model = models.Cart
        fields = []



class OrderForm(forms.ModelForm):
    class Meta:
        model = models.Order
        fields = []



class OrderItemForm(forms.ModelForm):
    class Meta:
        model = models.OrderItem
        fields = []


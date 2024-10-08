from django.db import models
from django.urls import reverse


class Cart(models.Model):
    # Fields
    product_variant = models.ForeignKey('products.ProductVariant', models.CASCADE)
    user = models.ForeignKey('users.User', models.CASCADE, related_name='carts')
    created = models.DateTimeField(auto_now_add=True, editable=False)

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)


class Order(models.Model):
    # Fields
    user = models.ForeignKey('users.User', models.CASCADE)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    created = models.DateTimeField(auto_now_add=True, editable=False)

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)


class OrderItem(models.Model):
    # Fields
    order = models.ForeignKey('Order', models.CASCADE)
    product_variant = models.ForeignKey('products.ProductVariant', models.CASCADE)

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

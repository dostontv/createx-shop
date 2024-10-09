from django.db import models

from apps.orders.utils import generate_uuid_v4


class Cart(models.Model):
    # Fields
    product_variant = models.ForeignKey('products.ProductVariant', models.CASCADE)
    user = models.ForeignKey('users.User', models.CASCADE, related_name='carts')
    quantity = models.PositiveSmallIntegerField(db_default=1)
    created = models.DateTimeField(auto_now_add=True, editable=False)

    class Meta:
        db_table = 'cart'

    def __str__(self):
        return str(self.pk)


class Order(models.Model):
    uid = models.UUIDField(primary_key=True, default=generate_uuid_v4, editable=False)

    class StatusType(models.TextChoices):
        APPROVED = 'approved', 'APPROVED'
        PENDING = 'pending', 'PENDING'
        CANCELLED = 'cancelled', 'CANCELLED'

    class TXNType(models.TextChoices):
        pass

    user = models.ForeignKey('users.User', models.CASCADE)
    status = models.CharField(max_length=25, choices=StatusType.choices, default=StatusType.PENDING)
    txn_status = models.CharField(max_length=20)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        db_table = 'orders'

    def __str__(self):
        return str(self.pk)


class OrderItem(models.Model):
    # Fields
    order = models.ForeignKey('Order', models.CASCADE)
    product_variant = models.ForeignKey('products.ProductVariant', models.CASCADE)
    quantity = models.PositiveSmallIntegerField(db_default=1)

    class Meta:
        db_table = 'orderItem'

    def __str__(self):
        return str(self.pk)

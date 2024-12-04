from django.db import models


class ProductVariant(models.Model):
    price = models.FloatField()
    quantity = models.SmallIntegerField()
    size = models.ForeignKey('products.Size', models.CASCADE, null=True, blank=True)
    color = models.ForeignKey('products.Color', models.CASCADE)
    material = models.ForeignKey('products.Material', models.SET_NULL, blank=True, null=True)
    brand = models.ForeignKey('products.Brand', models.SET_NULL, blank=True, null=True)
    product = models.ForeignKey('products.Product', models.CASCADE, "variants")
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        db_table = 'productVariants'

    def __str__(self):
        return str(self.pk)

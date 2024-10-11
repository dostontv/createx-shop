from django.db import models


class ProductVariant(models.Model):
    quantity = models.SmallIntegerField()
    price = models.FloatField()
    size = models.ForeignKey('products.Size', models.CASCADE)
    color = models.ForeignKey('products.Color', models.CASCADE)
    product = models.ForeignKey('products.Product', models.CASCADE, "variants")
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        db_table = 'productVariants'

    def __str__(self):
        return str(self.pk)

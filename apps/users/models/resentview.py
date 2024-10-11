from django.db import models


class ResentView(models.Model):
    # Fields
    user = models.ForeignKey("users.User", models.CASCADE)
    product_variant = models.ForeignKey('products.ProductVariant', models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, editable=False)

    class Meta:
        db_table = 'resent'

    def __str__(self):
        return str(self.pk)



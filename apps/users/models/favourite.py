from django.db import models


class Favourite(models.Model):
    # Fields
    product_variant = models.ForeignKey("products.ProductVariant", models.CASCADE)
    user = models.ForeignKey("users.User", models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, editable=False)

    class Meta:
        db_table = "favourites"

    def __str__(self):
        return str(self.pk)

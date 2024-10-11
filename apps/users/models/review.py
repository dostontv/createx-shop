from django.db import models


class Review(models.Model):
    # Fields
    name = models.CharField(max_length=30)
    content = models.FileField(upload_to="upload/files/review/")
    rating = models.SmallIntegerField()
    product_variant = models.ForeignKey('products.ProductVariant', models.CASCADE, related_name="reviews")
    user = models.ForeignKey('users.User', models.CASCADE, related_name="reviews")
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        db_table = 'reviews'

    def __str__(self):
        return str(self.name)

from django.db import models
from mptt.fields import TreeForeignKey
from tinymce.models import HTMLField


class Product(models.Model):
    name = models.CharField(max_length=250)
    category = TreeForeignKey('products.Category', models.CASCADE, 'products')
    description = HTMLField()
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        db_table = 'products'

    def __str__(self):
        return f'{self.id} - {self.name}'

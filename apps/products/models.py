
from django.db import models
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel
from tinymce.models import HTMLField


class Category(MPTTModel):
    # Fields
    name = models.CharField(max_length=30)
    parent = TreeForeignKey("self", models.CASCADE, related_name="children", null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        pass

    def __str__(self):
        return str(self.name)


class Size(models.Model):
    # Fields
    name = models.CharField(max_length=30)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    created = models.DateTimeField(auto_now_add=True, editable=False)

    class Meta:
        pass

    def __str__(self):
        return str(self.name)


class Color(models.Model):
    # Fields
    name = models.CharField(max_length=30)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        pass

    def __str__(self):
        return str(self.name)


class Product(models.Model):
    # Fields
    name = models.CharField(max_length=30)
    category = models.ForeignKey("Category", models.CASCADE, related_name="products")
    description = HTMLField()
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        pass

    def __str__(self):
        return f'{self.id} - {self.name}'


class ProductVariant(models.Model):
    # Fields
    quantity = models.SmallIntegerField()
    price = models.FloatField()
    size = models.ForeignKey('Size', models.CASCADE)
    color = models.ForeignKey('Color', models.CASCADE)
    product = models.ForeignKey('Product', models.CASCADE, related_name="variants")
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)


class Content(models.Model):
    # Fields
    content = models.FileField(upload_to="upload/files/")
    product_variant = models.ForeignKey("ProductVariant", models.CASCADE, related_name="content")
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        pass

    def __str__(self):
        return f'{self.pk}'

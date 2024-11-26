from django.db import models


class Size(models.Model):
    # Fields
    name = models.CharField(max_length=30)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    created = models.DateTimeField(auto_now_add=True, editable=False)

    class Meta:
        db_table = 'sizes'

    def __str__(self):
        return str(self.name)


class Color(models.Model):
    # Fields
    name = models.CharField(max_length=30)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        db_table = 'colors'

    def __str__(self):
        return str(self.name)


class Content(models.Model):
    content = models.FileField(upload_to='upload/files/')
    product_variant = models.ForeignKey('products.ProductVariant', models.CASCADE, related_name='content')
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        db_table = 'content'

    def __str__(self):
        return f'{self.pk}'


class Material(models.Model):
    name = models.CharField(max_length=30)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        db_table = 'materials'

    def __str__(self):
        return f'{self.id} - ' + self.name


class Brand(models.Model):
    name = models.CharField(max_length=30)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        db_table = 'brands'

    def __str__(self):
        return f'{self.id} - ' + self.name

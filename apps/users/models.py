from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse

from apps.users.managers import CustomUserManager


class Favourite(models.Model):
    # Fields
    product_variant = models.ForeignKey("products.ProductVariant", models.CASCADE)
    user = models.ForeignKey("users.User", models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, editable=False)

    class Meta:
        db_table = "favourites"

    def __str__(self):
        return str(self.pk)


class ResentView(models.Model):
    # Fields
    user = models.ForeignKey("users.User", models.CASCADE)
    product_variant = models.ForeignKey('products.ProductVariant', models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, editable=False)

    class Meta:
        db_table = 'resent'

    def __str__(self):
        return str(self.pk)


class User(AbstractUser):
    # Fields
    username_validator = None
    username = None
    email = models.EmailField(unique=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = CustomUserManager()

    class Meta:
        db_table = 'users'

    def __str__(self):
        return str(self.pk)


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

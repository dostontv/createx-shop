from django.contrib.auth.models import AbstractUser
from django.db import models

from apps.users.managers import CustomUserManager


class User(AbstractUser):
    # Fields
    username_validator = None
    username = None
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, unique=True, null=True, db_default="+998")
    country = models.CharField(max_length=50, null=True, db_default="")
    city = models.CharField(max_length=50, null=True, db_default="")
    address = models.TextField(null=True, db_default="")
    zip_code = models.CharField(max_length=15, null=True, db_default="")
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = CustomUserManager()

    class Meta:
        db_table = 'users'
        unique_together = [
            ('email', 'is_active')
        ]

    def __str__(self):
        return str(self.pk)

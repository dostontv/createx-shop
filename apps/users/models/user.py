from django.contrib.auth.models import AbstractUser
from django.db import models

from apps.users.managers import CustomUserManager


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
        unique_together = [
            ('email', 'is_active')
        ]

    def __str__(self):
        return str(self.pk)

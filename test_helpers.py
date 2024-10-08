import random
import string

from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import Group
from django.contrib.contenttypes.models import ContentType

from apps.users import models as users_models
from apps.products import models as products_models
from apps.orders import models as orders_models


def random_string(length=10):
    # Create a random string of length length
    letters = string.ascii_lowercase
    return "".join(random.choice(letters) for i in range(length))


def create_User(**kwargs):
    defaults = {
        "username": "%s_username" % random_string(5),
        "email": "%s_username@tempurl.com" % random_string(5),
    }
    defaults.update(**kwargs)
    return User.objects.create(**defaults)


def create_AbstractUser(**kwargs):
    defaults = {
        "username": "%s_username" % random_string(5),
        "email": "%s_username@tempurl.com" % random_string(5),
    }
    defaults.update(**kwargs)
    return AbstractUser.objects.create(**defaults)


def create_AbstractBaseUser(**kwargs):
    defaults = {
        "username": "%s_username" % random_string(5),
        "email": "%s_username@tempurl.com" % random_string(5),
    }
    defaults.update(**kwargs)
    return AbstractBaseUser.objects.create(**defaults)


def create_Group(**kwargs):
    defaults = {
        "name": "%s_group" % random_string(5),
    }
    defaults.update(**kwargs)
    return Group.objects.create(**defaults)


def create_ContentType(**kwargs):
    defaults = {
    }
    defaults.update(**kwargs)
    return ContentType.objects.create(**defaults)


def create_users_Favourite(**kwargs):
    defaults = {}
    defaults.update(**kwargs)
    return users_models.Favourite.objects.create(**defaults)
def create_users_ResentView(**kwargs):
    defaults = {}
    defaults.update(**kwargs)
    return users_models.ResentView.objects.create(**defaults)
def create_users_User(**kwargs):
    defaults = {}
    defaults["username"] = "username"
    defaults["email"] = "username@tempurl.com"
    defaults.update(**kwargs)
    return users_models.User.objects.create(**defaults)
def create_products_Category(**kwargs):
    defaults = {}
    defaults["name"] = ""
    defaults.update(**kwargs)
    return products_models.Category.objects.create(**defaults)
def create_products_Color(**kwargs):
    defaults = {}
    defaults["name"] = ""
    defaults.update(**kwargs)
    return products_models.Color.objects.create(**defaults)
def create_products_Content(**kwargs):
    defaults = {}
    defaults["content"] = ""
    defaults.update(**kwargs)
    return products_models.Content.objects.create(**defaults)
def create_products_Product(**kwargs):
    defaults = {}
    defaults["description"] = ""
    defaults["name"] = ""
    defaults.update(**kwargs)
    return products_models.Product.objects.create(**defaults)
def create_products_ProductVariant(**kwargs):
    defaults = {}
    defaults["quantity"] = ""
    defaults["price"] = ""
    defaults.update(**kwargs)
    return products_models.ProductVariant.objects.create(**defaults)
def create_products_Review(**kwargs):
    defaults = {}
    defaults["name"] = ""
    defaults["content"] = ""
    defaults["rating"] = ""
    defaults.update(**kwargs)
    return products_models.Review.objects.create(**defaults)
def create_products_Size(**kwargs):
    defaults = {}
    defaults["name"] = ""
    defaults.update(**kwargs)
    return products_models.Size.objects.create(**defaults)
def create_orders_Cart(**kwargs):
    defaults = {}
    defaults.update(**kwargs)
    return orders_models.Cart.objects.create(**defaults)
def create_orders_Order(**kwargs):
    defaults = {}
    defaults.update(**kwargs)
    return orders_models.Order.objects.create(**defaults)
def create_orders_OrderItem(**kwargs):
    defaults = {}
    defaults.update(**kwargs)
    return orders_models.OrderItem.objects.create(**defaults)

import pytest
import test_helpers

from django.urls import reverse


pytestmark = [pytest.mark.django_db]


def tests_Category_list_view(client):
    instance1 = test_helpers.create_products_Category()
    instance2 = test_helpers.create_products_Category()
    url = reverse("products_Category_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_Category_create_view(client):
    url = reverse("products_Category_create")
    data = {
        "name": "text",
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Category_detail_view(client):
    instance = test_helpers.create_products_Category()
    url = reverse("products_Category_detail", args=[instance.pk, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_Category_update_view(client):
    instance = test_helpers.create_products_Category()
    url = reverse("products_Category_update", args=[instance.pk, ])
    data = {
        "name": "text",
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Color_list_view(client):
    instance1 = test_helpers.create_products_Color()
    instance2 = test_helpers.create_products_Color()
    url = reverse("products_Color_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_Color_create_view(client):
    url = reverse("products_Color_create")
    data = {
        "name": "text",
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Color_detail_view(client):
    instance = test_helpers.create_products_Color()
    url = reverse("products_Color_detail", args=[instance.pk, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_Color_update_view(client):
    instance = test_helpers.create_products_Color()
    url = reverse("products_Color_update", args=[instance.pk, ])
    data = {
        "name": "text",
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Content_list_view(client):
    instance1 = test_helpers.create_products_Content()
    instance2 = test_helpers.create_products_Content()
    url = reverse("products_Content_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_Content_create_view(client):
    url = reverse("products_Content_create")
    data = {
        "content": "aFile",
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Content_detail_view(client):
    instance = test_helpers.create_products_Content()
    url = reverse("products_Content_detail", args=[instance.pk, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_Content_update_view(client):
    instance = test_helpers.create_products_Content()
    url = reverse("products_Content_update", args=[instance.pk, ])
    data = {
        "content": "aFile",
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Product_list_view(client):
    instance1 = test_helpers.create_products_Product()
    instance2 = test_helpers.create_products_Product()
    url = reverse("products_Product_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_Product_create_view(client):
    url = reverse("products_Product_create")
    data = {
        "description": "text",
        "name": "text",
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Product_detail_view(client):
    instance = test_helpers.create_products_Product()
    url = reverse("products_Product_detail", args=[instance.pk, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_Product_update_view(client):
    instance = test_helpers.create_products_Product()
    url = reverse("products_Product_update", args=[instance.pk, ])
    data = {
        "description": "text",
        "name": "text",
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_ProductVariant_list_view(client):
    instance1 = test_helpers.create_products_ProductVariant()
    instance2 = test_helpers.create_products_ProductVariant()
    url = reverse("products_ProductVariant_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_ProductVariant_create_view(client):
    url = reverse("products_ProductVariant_create")
    data = {
        "quantity": 1,
        "price": 1.0,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_ProductVariant_detail_view(client):
    instance = test_helpers.create_products_ProductVariant()
    url = reverse("products_ProductVariant_detail", args=[instance.pk, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_ProductVariant_update_view(client):
    instance = test_helpers.create_products_ProductVariant()
    url = reverse("products_ProductVariant_update", args=[instance.pk, ])
    data = {
        "quantity": 1,
        "price": 1.0,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Review_list_view(client):
    instance1 = test_helpers.create_products_Review()
    instance2 = test_helpers.create_products_Review()
    url = reverse("products_Review_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_Review_create_view(client):
    url = reverse("products_Review_create")
    data = {
        "name": "text",
        "content": "aFile",
        "rating": 1,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Review_detail_view(client):
    instance = test_helpers.create_products_Review()
    url = reverse("products_Review_detail", args=[instance.pk, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_Review_update_view(client):
    instance = test_helpers.create_products_Review()
    url = reverse("products_Review_update", args=[instance.pk, ])
    data = {
        "name": "text",
        "content": "aFile",
        "rating": 1,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Size_list_view(client):
    instance1 = test_helpers.create_products_Size()
    instance2 = test_helpers.create_products_Size()
    url = reverse("products_Size_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_Size_create_view(client):
    url = reverse("products_Size_create")
    data = {
        "name": "text",
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Size_detail_view(client):
    instance = test_helpers.create_products_Size()
    url = reverse("products_Size_detail", args=[instance.pk, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_Size_update_view(client):
    instance = test_helpers.create_products_Size()
    url = reverse("products_Size_update", args=[instance.pk, ])
    data = {
        "name": "text",
    }
    response = client.post(url, data)
    assert response.status_code == 302

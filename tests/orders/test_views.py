import pytest
import test_helpers

from django.urls import reverse


pytestmark = [pytest.mark.django_db]


def tests_Cart_list_view(client):
    instance1 = test_helpers.create_orders_Cart()
    instance2 = test_helpers.create_orders_Cart()
    url = reverse("orders_Cart_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_Cart_create_view(client):
    url = reverse("orders_Cart_create")
    data = {
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Cart_detail_view(client):
    instance = test_helpers.create_orders_Cart()
    url = reverse("orders_Cart_detail", args=[instance.pk, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_Cart_update_view(client):
    instance = test_helpers.create_orders_Cart()
    url = reverse("orders_Cart_update", args=[instance.pk, ])
    data = {
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Order_list_view(client):
    instance1 = test_helpers.create_orders_Order()
    instance2 = test_helpers.create_orders_Order()
    url = reverse("orders_Order_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_Order_create_view(client):
    url = reverse("orders_Order_create")
    data = {
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Order_detail_view(client):
    instance = test_helpers.create_orders_Order()
    url = reverse("orders_Order_detail", args=[instance.pk, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_Order_update_view(client):
    instance = test_helpers.create_orders_Order()
    url = reverse("orders_Order_update", args=[instance.pk, ])
    data = {
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_OrderItem_list_view(client):
    instance1 = test_helpers.create_orders_OrderItem()
    instance2 = test_helpers.create_orders_OrderItem()
    url = reverse("orders_OrderItem_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_OrderItem_create_view(client):
    url = reverse("orders_OrderItem_create")
    data = {
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_OrderItem_detail_view(client):
    instance = test_helpers.create_orders_OrderItem()
    url = reverse("orders_OrderItem_detail", args=[instance.pk, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_OrderItem_update_view(client):
    instance = test_helpers.create_orders_OrderItem()
    url = reverse("orders_OrderItem_update", args=[instance.pk, ])
    data = {
    }
    response = client.post(url, data)
    assert response.status_code == 302

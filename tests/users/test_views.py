import pytest
import test_helpers

from django.urls import reverse


pytestmark = [pytest.mark.django_db]


def tests_Favourite_list_view(client):
    instance1 = test_helpers.create_users_Favourite()
    instance2 = test_helpers.create_users_Favourite()
    url = reverse("users_Favourite_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_Favourite_create_view(client):
    url = reverse("users_Favourite_create")
    data = {
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Favourite_detail_view(client):
    instance = test_helpers.create_users_Favourite()
    url = reverse("users_Favourite_detail", args=[instance.pk, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_Favourite_update_view(client):
    instance = test_helpers.create_users_Favourite()
    url = reverse("users_Favourite_update", args=[instance.pk, ])
    data = {
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_ResentView_list_view(client):
    instance1 = test_helpers.create_users_ResentView()
    instance2 = test_helpers.create_users_ResentView()
    url = reverse("users_ResentView_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_ResentView_create_view(client):
    url = reverse("users_ResentView_create")
    data = {
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_ResentView_detail_view(client):
    instance = test_helpers.create_users_ResentView()
    url = reverse("users_ResentView_detail", args=[instance.pk, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_ResentView_update_view(client):
    instance = test_helpers.create_users_ResentView()
    url = reverse("users_ResentView_update", args=[instance.pk, ])
    data = {
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_User_list_view(client):
    instance1 = test_helpers.create_users_User()
    instance2 = test_helpers.create_users_User()
    url = reverse("users_User_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_User_create_view(client):
    url = reverse("users_User_create")
    data = {
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_User_detail_view(client):
    instance = test_helpers.create_users_User()
    url = reverse("users_User_detail", args=[instance.pk, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_User_update_view(client):
    instance = test_helpers.create_users_User()
    url = reverse("users_User_update", args=[instance.pk, ])
    data = {
    }
    response = client.post(url, data)
    assert response.status_code == 302

from rest_framework import serializers

from . import models


class FavouriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Favourite
        fields = [
            "product_variant",
            "user",
            "created",
        ]


class ResentViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ResentView
        fields = [
            "product_variant",
            "created",
            "user",
        ]


class UserRetrieveAPISerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = [
            "first_name",
            "last_name",
            "email",
            "last_updated",
            "created",
        ]


class UserCreateSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = models.User
        fields = [
            "first_name",
            "last_name",
            "email",
            "password1",
            "password2",
        ]


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Review
        fields = [
            "last_updated",
            "name",
            "product_variant",
            "content",
            "created",
            "rating",
            "user_id",
        ]

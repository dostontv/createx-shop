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


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = [
            "last_updated",
            "created",
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

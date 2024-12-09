from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from . import models
from .utils import generate_one_time_verification


class FavouriteListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Favourite
        fields = [
            "product_variant",
            "user",
        ]


# Serializer for creating Favourite objects
class FavouriteCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Favourite
        fields = [
            "product_variant",
            "user",
        ]


# Serializer for retrieving a Favourite object
class FavouriteRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Favourite
        fields = [
            "product_variant",
            "user",
            "created",
        ]


# Serializer for updating Favourite objects (partial update if required)
class FavouriteUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Favourite
        fields = [
            "product_variant",  # Allow partial updates for these fields
            "user",
            "created",
        ]


# ResentView Serializers

# Serializer for listing ResentView objects
class ResentViewListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ResentView
        fields = [
            "product_variant",
            "user",
        ]


# Serializer for creating ResentView objects
class ResentViewCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ResentView
        fields = [
            "product_variant",  # All fields needed for creation
            "user",
        ]


# Serializer for retrieving a ResentView object
class ResentViewRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ResentView
        fields = [
            "product_variant",
            "user",
            "created",
        ]


# Serializer for updating ResentView objects (partial update if required)
class ResentViewUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ResentView
        fields = [
            "product_variant",  # Allow partial updates
            "user",
            "created",
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

    def validate(self, data):
        if data['password1'] != data['password2']:
            raise serializers.ValidationError("Passwords do not match.")

        try:
            validate_password(data['password1'])
        except ValidationError as e:
            raise serializers.ValidationError({"password1": list(e.messages)})

        return data

    def create(self, validated_data):
        password = validated_data.pop('password1')
        validated_data.pop('password2')
        request = validated_data.pop('request')

        user = models.User.objects.create(**validated_data)
        user.set_password(password)
        user.is_active = False
        user.save()

        if request:
            generate_one_time_verification(request, user)

        return user




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
            "user_id"
        ]

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
    full_name = serializers.CharField()

    class Meta:
        model = models.User
        fields = [
            "full_name",
            "email",
            "password",
        ]
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def validate(self, data):
        try:
            validate_password(data['password'])
        except ValidationError as e:
            raise serializers.ValidationError({"password": list(e.messages)})

        return data

    def create(self, validated_data):
        full_name = validated_data.pop('full_name')
        password = validated_data.pop('password')
        request = validated_data.pop('request')

        full_name = full_name.split()

        user = models.User.objects.create(**validated_data)
        user.first_name = full_name[0]
        if len(full_name) > 1:
            user.last_name = full_name[1]
        user.set_password(password)
        user.is_active = False
        user.save()

        if request:
            generate_one_time_verification(request, user)

        user.full_name = ' '.join(full_name)
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

from django.utils.encoding import force_str
from django.utils.http import urlsafe_base64_decode
from drf_spectacular.utils import extend_schema
from rest_framework import viewsets, permissions, generics
from rest_framework.response import Response
from rest_framework.views import APIView

from . import models
from . import serializers
from .tokens import account_activation_token


@extend_schema(tags=['Favourite'])
class FavouriteListAPIView(generics.ListAPIView):
    queryset = models.Favourite.objects.all()
    serializer_class = serializers.FavouriteListSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)


# Create View for Favourite
@extend_schema(tags=['Favourite'])
class FavouriteCreateAPIView(generics.CreateAPIView):
    queryset = models.Favourite.objects.all()
    serializer_class = serializers.FavouriteCreateSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


# Retrieve View for Favourite
@extend_schema(tags=['Favourite'])
class FavouriteRetrieveAPIView(generics.RetrieveAPIView):
    queryset = models.Favourite.objects.all()
    serializer_class = serializers.FavouriteRetrieveSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)


# Update View for Favourite
@extend_schema(tags=['Favourite'])
class FavouriteUpdateAPIView(generics.UpdateAPIView):
    queryset = models.Favourite.objects.all()
    serializer_class = serializers.FavouriteUpdateSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)


# Delete View for Favourite
@extend_schema(tags=['Favourite'])
class FavouriteDeleteAPIView(generics.DestroyAPIView):
    queryset = models.Favourite.objects.all()
    serializer_class = serializers.FavouriteListSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)


# List View for ResentView
@extend_schema(tags=['ResentView'])
class ResentViewListAPIView(generics.ListAPIView):
    queryset = models.ResentView.objects.all()
    serializer_class = serializers.ResentViewListSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)


# Create View for ResentView
@extend_schema(tags=['ResentView'])
class ResentViewCreateAPIView(generics.CreateAPIView):
    queryset = models.ResentView.objects.all()
    serializer_class = serializers.ResentViewCreateSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


# Retrieve View for ResentView
@extend_schema(tags=['ResentView'])
class ResentViewRetrieveAPIView(generics.RetrieveAPIView):
    queryset = models.ResentView.objects.all()
    serializer_class = serializers.ResentViewRetrieveSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)


# Update View for ResentView
@extend_schema(tags=['ResentView'])
class ResentViewUpdateAPIView(generics.UpdateAPIView):
    queryset = models.ResentView.objects.all()
    serializer_class = serializers.ResentViewUpdateSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)


# Delete View for ResentView
@extend_schema(tags=['ResentView'])
class ResentViewDeleteAPIView(generics.DestroyAPIView):
    queryset = models.ResentView.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = serializers.ResentViewListSerializer

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)


@extend_schema(tags=['User'])
class UserRetrieveAPIView(generics.RetrieveAPIView):
    queryset = models.User.objects.all()
    serializer_class = serializers.UserRetrieveAPISerializer
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        self.kwargs['pk'] = request.user.id
        return super().get(request, *args, **kwargs)


@extend_schema(tags=['User'])
class UserUpdateAPIView(generics.UpdateAPIView):
    queryset = models.User.objects.all()
    serializer_class = serializers.UserRetrieveAPISerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        self.kwargs['pk'] = self.request.user.id
        return super().get_object()

@extend_schema(tags=['User'])
class UserDestroyAPIView(generics.DestroyAPIView):
    queryset = models.User.objects.all()
    serializer_class = serializers.UserDestroyAPISerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        self.kwargs['pk'] = self.request.user.id
        return super().get_object()

@extend_schema(tags=['User'])
class UserCreateAPIView(generics.CreateAPIView):
    queryset = models.User.objects.all()
    serializer_class = serializers.UserCreateSerializer

    def perform_create(self, serializer):
        serializer.validated_data['request'] = self.request
        super().perform_create(serializer)


@extend_schema(tags=['Review'])
class ReviewViewSet(viewsets.ModelViewSet):
    """ViewSet for the Review class"""

    queryset = models.Review.objects.all()
    serializer_class = serializers.ReviewSerializer
    permission_classes = [permissions.IsAuthenticated]


class VerifyEmailConfirm(APIView):
    serializer_class = serializers.VerifyEmailConfirmSerializer

    def get(self, request, uidb64, token):
        try:
            uid = force_str(urlsafe_base64_decode(uidb64))
            user = models.User.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, models.User.DoesNotExist):
            user = None
        if user is not None and account_activation_token.check_token(user, token):
            user.is_active = True
            user.save()
            return Response({"Your email has been verified"})
        else:
            return Response({"message": "The link is invalid"})

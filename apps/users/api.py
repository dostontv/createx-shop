from drf_spectacular.utils import extend_schema
from rest_framework import viewsets, permissions, generics

from . import models
from . import serializers


@extend_schema(tags=['Favourite'])
class FavouriteViewSet(viewsets.ModelViewSet):
    """ViewSet for the Favourite class"""

    queryset = models.Favourite.objects.all()
    serializer_class = serializers.FavouriteSerializer
    permission_classes = [permissions.IsAuthenticated]


@extend_schema(tags=['ResentView'])
class ResentViewViewSet(viewsets.ModelViewSet):
    """ViewSet for the ResentView class"""

    queryset = models.ResentView.objects.all()
    serializer_class = serializers.ResentViewSerializer
    permission_classes = [permissions.IsAuthenticated]


@extend_schema(tags=['User'])
class UserRetrieveAPIView(generics.RetrieveAPIView):
    queryset = models.User.objects.all()
    serializer_class = serializers.UserRetrieveAPISerializer
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        self.kwargs['pk'] = request.user.id
        return super().get(request, *args, **kwargs)


@extend_schema(tags=['User'])
class UserCreateAPIView(generics.CreateAPIView):
    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializer



@extend_schema(tags=['Review'])
class ReviewViewSet(viewsets.ModelViewSet):
    """ViewSet for the Review class"""

    queryset = models.Review.objects.all()
    serializer_class = serializers.ReviewSerializer
    permission_classes = [permissions.IsAuthenticated]

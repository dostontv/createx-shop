from rest_framework import viewsets, permissions, generics

from . import models
from . import serializers


class FavouriteViewSet(viewsets.ModelViewSet):
    """ViewSet for the Favourite class"""

    queryset = models.Favourite.objects.all()
    serializer_class = serializers.FavouriteSerializer
    permission_classes = [permissions.IsAuthenticated]


class ResentViewViewSet(viewsets.ModelViewSet):
    """ViewSet for the ResentView class"""

    queryset = models.ResentView.objects.all()
    serializer_class = serializers.ResentViewSerializer
    permission_classes = [permissions.IsAuthenticated]


class UserRetrieveAPIView(generics.RetrieveAPIView):
    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        self.kwargs['pk'] = request.user.id
        return super().get(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)


class ReviewViewSet(viewsets.ModelViewSet):
    """ViewSet for the Review class"""

    queryset = models.Review.objects.all()
    serializer_class = serializers.ReviewSerializer
    permission_classes = [permissions.IsAuthenticated]

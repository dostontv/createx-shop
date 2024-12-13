from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from . import api
from .api import VerifyEmailConfirm

router = routers.DefaultRouter()

urlpatterns = (
    path("", include(router.urls)),
    path('User/me/', api.UserRetrieveAPIView.as_view()),
    path('User/add/', api.UserCreateAPIView.as_view()),
    path('User/update/', api.UserUpdateAPIView.as_view()),
    path('User/delete/', api.UserDestroyAPIView.as_view()),
    path('verify-email-confirm/<uidb64>/<token>', VerifyEmailConfirm.as_view(), name='verify-email-confirm'),

    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('favourites/', api.FavouriteListAPIView.as_view(), name='favourite-list'),
    path('favourites/create/', api.FavouriteCreateAPIView.as_view(), name='favourite-create'),
    path('favourites/<int:pk>/', api.FavouriteRetrieveAPIView.as_view(), name='favourite-retrieve'),
    path('favourites/update/<int:pk>/', api.FavouriteUpdateAPIView.as_view(), name='favourite-update'),
    path('favourites/delete/<int:pk>/', api.FavouriteDeleteAPIView.as_view(), name='favourite-delete'),

    path('resentviews/', api.ResentViewListAPIView.as_view(), name='resentview-list'),
    path('resentviews/create/', api.ResentViewCreateAPIView.as_view(), name='resentview-create'),
    path('resentviews/<int:pk>/', api.ResentViewRetrieveAPIView.as_view(), name='resentview-retrieve'),
    path('resentviews/update/<int:pk>/', api.ResentViewUpdateAPIView.as_view(), name='resentview-update'),
    path('resentviews/delete/<int:pk>/', api.ResentViewDeleteAPIView.as_view(), name='resentview-delete'),

)

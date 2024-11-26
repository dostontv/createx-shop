from django.contrib import admin
from django import forms

from . import models


class FavouriteAdminForm(forms.ModelForm):
    class Meta:
        model = models.Favourite
        fields = "__all__"


class FavouriteAdmin(admin.ModelAdmin):
    form = FavouriteAdminForm
    list_display = [
        "user",
        "created",
    ]


class ResentViewAdminForm(forms.ModelForm):
    class Meta:
        model = models.ResentView
        fields = "__all__"


class ResentViewAdmin(admin.ModelAdmin):
    form = ResentViewAdminForm
    list_display = [
        "created",
        "user",
    ]


class UserAdminForm(forms.ModelForm):
    class Meta:
        model = models.User
        fields = "__all__"


class UserAdmin(admin.ModelAdmin):
    form = UserAdminForm
    list_display = [
        "id",
        "first_name",
    ]


class ReviewAdminForm(forms.ModelForm):
    class Meta:
        model = models.Review
        fields = "__all__"


class ReviewAdmin(admin.ModelAdmin):
    form = ReviewAdminForm
    list_display = [
        "name",
        "content",
        "created",
        "rating",
        "user_id",
    ]


admin.site.register(models.Favourite, FavouriteAdmin)
admin.site.register(models.ResentView, ResentViewAdmin)
admin.site.register(models.User, UserAdmin)
admin.site.register(models.Review, ReviewAdmin)

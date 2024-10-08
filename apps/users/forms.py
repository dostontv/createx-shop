from django import forms
from . import models


class FavouriteForm(forms.ModelForm):
    class Meta:
        model = models.Favourite
        fields = []



class ResentViewForm(forms.ModelForm):
    class Meta:
        model = models.ResentView
        fields = []



class UserForm(forms.ModelForm):
    class Meta:
        model = models.User
        fields = []


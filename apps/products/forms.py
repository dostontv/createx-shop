from django import forms
from . import models


class CategoryForm(forms.ModelForm):
    class Meta:
        model = models.Category
        fields = [
            "name",
        ]


class ColorForm(forms.ModelForm):
    class Meta:
        model = models.Color
        fields = [
            "name",
        ]


class ContentForm(forms.ModelForm):
    class Meta:
        model = models.Content
        fields = [
            "content",
        ]


class ProductForm(forms.ModelForm):
    class Meta:
        model = models.Product
        fields = [
            "description",
            "name",
        ]


class ProductVariantForm(forms.ModelForm):
    class Meta:
        model = models.ProductVariant
        fields = [
            "quantity",
            "price",
        ]


class ReviewForm(forms.ModelForm):
    class Meta:
        model = models.Review
        fields = [
            "name",
            "content",
            "rating",
        ]


class SizeForm(forms.ModelForm):
    class Meta:
        model = models.Size
        fields = [
            "name",
        ]

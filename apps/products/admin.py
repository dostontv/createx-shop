from django import forms
from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin

from . import models


class CategoryAdmin(DraggableMPTTAdmin):
    mptt_indent_field = 'name'
    list_display = ('tree_actions', 'indented_title',
                    'related_products_count', 'related_products_cumulative_count')
    list_display_links = ('indented_title',)

    def get_queryset(self, request):
        qs = super().get_queryset(request)

        qs = models.Category.objects.add_related_count(
            qs,
            models.Product,
            'category',
            'products_cumulative_count',
            cumulative=True)

        qs = models.Category.objects.add_related_count(qs, models.Product, 'category', 'products_count',
                                                       cumulative=False)
        return qs

    def related_products_count(self, instance):
        return instance.products_count

    related_products_count.short_description = 'Related products (for this specific category)'

    def related_products_cumulative_count(self, instance):
        return instance.products_cumulative_count

    related_products_cumulative_count.short_description = 'Related products (in tree)'


class ColorAdminForm(forms.ModelForm):
    class Meta:
        model = models.Color
        fields = '__all__'


class ColorAdmin(admin.ModelAdmin):
    form = ColorAdminForm
    list_display = [
        'name',
        'last_updated',
        'created',
    ]


class ProductAdminForm(forms.ModelForm):
    class Meta:
        model = models.Product
        fields = '__all__'


class ProductAdmin(admin.ModelAdmin):
    form = ProductAdminForm
    list_display = [
        'name',
        'category',
        'created',
        'last_updated',
    ]


class ProductVContentStackedInline(admin.StackedInline):
    model = models.Content
    fields = 'content',
    extra = 1
    min_num = 1
    max_num = 5


class ProductVariantAdminForm(forms.ModelForm):
    class Meta:
        model = models.ProductVariant
        fields = '__all__'


class ProductVariantAdmin(admin.ModelAdmin):
    form = ProductVariantAdminForm
    inlines = [ProductVContentStackedInline]
    list_display = [
        'quantity',
        'color',
        'price',
        'product',
        'size',
        'created',
        'last_updated',
    ]


class SizeAdminForm(forms.ModelForm):
    class Meta:
        model = models.Size
        fields = '__all__'


class SizeAdmin(admin.ModelAdmin):
    form = SizeAdminForm
    list_display = [
        'name',
        'last_updated',
        'created',
    ]


admin.site.register(models.Category, CategoryAdmin)
admin.site.register(models.Color, ColorAdmin)
admin.site.register(models.Product, ProductAdmin)
admin.site.register(models.ProductVariant, ProductVariantAdmin)
admin.site.register(models.Size, SizeAdmin)

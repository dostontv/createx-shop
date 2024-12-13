import django_filters

from apps.products.models import Category, ProductVariant
from apps.products.utils import categories_id


class ProductFilter(django_filters.FilterSet):
    category = django_filters.NumberFilter(method='filter_by_category', help_text='Categories filter for all products')
    size = django_filters.NumberFilter(field_name='size', lookup_expr='exact')
    color = django_filters.NumberFilter(field_name='color', lookup_expr='exact')
    material = django_filters.NumberFilter(field_name='material', lookup_expr='exact')
    brand = django_filters.NumberFilter(field_name='brand', lookup_expr='exact')
    price = django_filters.RangeFilter(field_name='price')

    class Meta:
        model = ProductVariant
        fields = 'price', 'size', 'color', 'material', 'brand'

    def filter_by_category(self, queryset, name, value):
        category_lists = categories_id(Category.objects.get(id=int(value)), [])

        return queryset.filter(product__category__id__in=category_lists)

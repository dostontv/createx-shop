import django_filters

from apps.products.models import Category, ProductVariant
from apps.products.utils import categories_id


class ProductFilter(django_filters.FilterSet):
    category = django_filters.NumberFilter(method='filter_by_category', help_text='Categories filter for all products')

    class Meta:
        model = ProductVariant
        fields = 'price',

    def filter_by_category(self, queryset, name, value):
        category_lists = categories_id(Category.objects.get(id=int(value)), [])

        return queryset.filter(product__category__id__in=category_lists)

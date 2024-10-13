import django_filters

from apps.products.models import Product, Category
from apps.products.utils import categories_id


class ProductFilter(django_filters.FilterSet):
    category = django_filters.CharFilter(method='filter_by_category')

    class Meta:
        model = Product
        fields = 'name',

    def filter_by_category(self, queryset, name, value):
        category_lists = categories_id(Category.objects.get(id=int(value)), [])

        return queryset.filter(category_id__in=category_lists)

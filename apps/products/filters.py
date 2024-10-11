import django_filters

from apps.products.models import Product, Category


class ProductFilter(django_filters.FilterSet):
    category = django_filters.CharFilter(method='filter_by_category')

    class Meta:
        model = Product
        # fields = '__all__'
        exclude = 'category'

    def filter_by_category(self, queryset, name, value):

        pass

from django.db import models
from django.forms import ModelChoiceField
from mptt.forms import TreeNodeChoiceFieldMixin
from mptt.settings import DEFAULT_LEVEL_INDICATOR
from tinymce.models import HTMLField


class CustomTreeNodeChoiceFieldMixin(TreeNodeChoiceFieldMixin):
    def __init__(self, queryset, *args, **kwargs):
        self.level_indicator = kwargs.pop("level_indicator", DEFAULT_LEVEL_INDICATOR)
        self.start_level = kwargs.pop("start_level", 0)

        super().__init__(queryset, *args, **kwargs)


class TreeNodeChoiceField(CustomTreeNodeChoiceFieldMixin, ModelChoiceField):
    pass


class TreeForeignKey(models.ForeignKey):

    def formfield(self, **kwargs):
        kwargs.setdefault("form_class", TreeNodeChoiceField)
        return super().formfield(**kwargs)


class Product(models.Model):
    name = models.CharField(max_length=30)
    category = TreeForeignKey('products.Category', models.CASCADE, 'products')
    description = HTMLField()
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        db_table = 'products'

    def __str__(self):
        return f'{self.id} - {self.name}'

import django_filters
from .models import Mineral

import minerals.choices as choice


class MineralFilter(django_filters.FilterSet):

    group = django_filters.ChoiceFilter(
        label='Groups',
        choices=choice.GROUP_CHOICES,
        method='filter_by_group',
    )
    category = django_filters.ChoiceFilter(
        label='Category',
        choices=choice.CATEGORY_CHOICES,
        method='filter_by_category',
    )

    def filter_by_group(self, queryset, name, value):
        if name == 'Other':
            value = None
        else:
            value = value
        return queryset.filter(group=value)

    def filter_by_category(self, queryset, name, value):
        if name == 'Other':
            value = None
        else:
            value = value
        return queryset.filter(category=value)


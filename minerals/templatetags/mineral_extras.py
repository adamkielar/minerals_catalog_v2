from django import template

import minerals.choices as choice
from minerals.utils import random_mineral_footer

from minerals.models import Mineral

register = template.Library()


@register.simple_tag
def sort_letter():
    letters_filter = choice.LETTERS_FILTER
    return letters_filter


@register.simple_tag
def random_mineral():
    random_pk = random_mineral_footer(Mineral.objects.values().order_by('?'))
    return random_pk

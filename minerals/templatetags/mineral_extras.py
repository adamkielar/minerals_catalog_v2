from django import template
from django.template import Context, RequestContext
from django.urls import reverse, NoReverseMatch
from django.utils.encoding import escape_uri_path

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


@register.simple_tag(takes_context=True)
def active_letter(context, *args, **kwargs):
    request = context.get('request')
    request_path = request.path[8:9]
    if request_path == 'A':
        return 'active'
    else:
        return ''


    #request_context = RequestContext(request)
    #print(request_context)

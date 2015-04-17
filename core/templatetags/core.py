# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.utils.html import strip_tags
from django.utils.safestring import mark_safe
from django import template

register = template.Library()


@register.filter
def text(value):
    """
    Remove tags e retorna texto seguro
    """
    return mark_safe(strip_tags(value))


# -*- coding:utf-8 -*-

from django.core.urlresolvers import reverse, resolve, Resolver404
from django.template.response import TemplateResponse
from django.utils.translation import ugettext_lazy as _


def menu_loader(request):
    """
    Monta o menu principal
    """

    return {'MENU': ''}


def navigation_teste(request):
    return {}

# -*- coding:utf-8 -*-

from django.utils.translation import ugettext_lazy as _
from django.contrib import admin
from core.models import ACTIVE, INACTIVE


def inactivate(self, request, queryset):
    queryset.update(active=INACTIVE)
inactivate.short_description = _(u"Não Exibir / Inativar")


def activate(self, request, queryset):
    queryset.update(active=ACTIVE)
activate.short_description = _(u"Exibir / Ativar")

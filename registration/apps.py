# -*- coding:utf-8 -*-

from django.utils.translation import ugettext_lazy as _
from django.apps import AppConfig

class RegistrationConfig(AppConfig):
    name = 'registration'
    verbose_name = _(u"Registro de Usuários")

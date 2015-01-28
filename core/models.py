# -*- coding:utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _

ACTIVE = 'Y'
INACTIVE = 'N'
CHOICE_ACTIVE = (
    ('Y', _(u"Sim")),
    ('N', _(u"Não")),
)

class CoreModel(models.Model):
    """
    Model Padrao
    """
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

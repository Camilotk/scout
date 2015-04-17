# -*- coding:utf-8 -*-

from django.utils.translation import ugettext_lazy as _
from django.db import models
from django.contrib.auth.models import User, Group

from core.models import CoreModel


PAGE_STATUS = (
    ('P', _(u"Publicado")),
    ('R', _(u"Rascunho")),
)

PAGE_TYPE = {
    'transparencia': {
        'name': _(u"Transparência"),
        'title': _(u"Transparência"),
    },

}


class Page(CoreModel):
    """
    Criar nova Pagina
    """

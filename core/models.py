# -*- coding:utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from django.conf import settings

ACTIVE = 'Y'
INACTIVE = 'N'
CHOICE_ACTIVE = (
    ('Y', _(u"Sim")),
    ('N', _(u"Não")),
)

UF = (
    ('RS', _(u"Rio Grande do Sul"),),
    ('AC', _(u"Acre"),),
    ('AL', _(u"Alagoas"),),
    ('AP', _(u"Amapá"),),
    ('AM', _(u"Amazonas"),),
    ('BA', _(u"Bahia"),),
    ('CE', _(u"Ceará"),),
    ('DF', _(u"Distrito Federal"),),
    ('ES', _(u"Espírito Santo"),),
    ('GO', _(u"Goiás"),),
    ('MA', _(u"Maranhão"),),
    ('MT', _(u"Mato Grosso"),),
    ('MS', _(u"Mato Grosso do Sul"),),
    ('MG', _(u"Minas Gerais"),),
    ('PA', _(u"Pará"),),
    ('PB', _(u"Paraíba"),),
    ('PR', _(u"Paraná"),),
    ('PE', _(u"Pernambuco"),),
    ('PI', _(u"Piauí"),),
    ('RJ', _(u"Rio de Janeiro"),),
    ('RN', _(u"Rio Grande do Norte"),),
    ('RO', _(u"Rondônia"),),
    ('RR', _(u"Roraima"),),
    ('SC', _(u"Santa Catarina"),),
    ('SP', _(u"São Paulo"),),
    ('SE', _(u"Sergipe"),),
    ('TO', _(u"Tocantins"),),
)


def get_uf_dict():
    """
    Retorna para UF_DICT um dicionario com os estados, ex:
    {
        'RS': "Rio Grande do Sul",
        ...
    }
    """
    dic = {}
    for i in UF:
        dic[i[0]] = i[1].__unicode__()
    return dic

UF_DICT = get_uf_dict()


def get_valid_uf(uf_short_name):
    """
    Retorna a sigla do estado se o mesmo estiver correto e existir:
    """
    if UF_DICT.get(uf_short_name):
        return uf_short_name
    else:
        return ''



GROUP_ADMIN = u"Admin"
GROUP_LOBINHO = u"Lobinho"
GROUP_ESCOTEIRO = u"Escoteiro"
GROUP_SENIOR = u"Sênior"


class CoreModel(models.Model):
    """
    Model Padrao
    """
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True





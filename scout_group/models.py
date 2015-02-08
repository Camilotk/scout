# -*- coding:utf-8 -*-

from django.utils.translation import ugettext_lazy as _
from django.db import models
from django.contrib.auth.models import User
from core.models import CoreModel, CHOICE_ACTIVE, ACTIVE, UF


class ScoutGroup(CoreModel):
    """
    Cadastro de Grupos Escoteiros
    """
    name = models.CharField(verbose_name=_(u"Nome"), max_length=100, null=True, blank=True)
    number = models.IntegerField(verbose_name=_(u"Numeral"), null=False, blank=False)
    uf = models.CharField(verbose_name=_(u"UF"), max_length=2, choices=UF, null=False, blank=False, default=UF[0][0], help_text=_(u"Estado do Grupo Escoteiro."))
    active = models.CharField(verbose_name=_(u"Exibir"), max_length=1, choices=CHOICE_ACTIVE, default=ACTIVE, blank=False)

    class Meta:

        ordering = ["-name"]
        db_table = "scout_group"
        verbose_name = _(u"Grupo Escoteiro")
        verbose_name_plural = _(u"Grupos Escoteiros")

    def __unicode__(self):
        if not self.name:
            return "%0.3d - %s" % (self.number, self.uf)
        else:
            return "%s - %0.3d - %s" % (self.name, self.number, self.uf)

    def get_short_name(self):
        """
        Retorna somente numeral e sigla do estado
        """
        return "%0.3d - %s" % (self.number, self.uf)

class UserScoutGroup(models.Model):
    user = models.ForeignKey(to=User, null=False, blank=False, unique=True)
    scout_group = models.ForeignKey(to=ScoutGroup, null=False, blank=False)

    class Meta:
        ordering = ['user', 'scout_group']
        db_table = "scout_group_userscoutgroup"
        verbose_name = _(u"Usuário por Grupo Escoteiro")
        verbose_name_plural = _(u"Usuários por Grupo Escoteiro")

    def __unicode__(self):
        if self.user.first_name:
            return "%s %s" % (self.user.first_name, self.user.last_name)
        else:
            return self.user.username
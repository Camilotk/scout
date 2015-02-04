# -*- coding:utf-8 -*-

import os
from django.db import models
from django.contrib.auth.models import User, Group
from django.utils.translation import ugettext_lazy as _
from django.db.models.signals import pre_delete, pre_save
from django.dispatch.dispatcher import receiver
from django.conf import settings
from core.models import CoreModel, CHOICE_ACTIVE, ACTIVE
import uuid


class Branch(CoreModel):
    """
    Ramo
    """
    name = models.CharField(verbose_name=_(u"Nome"), max_length=100, null=False)
    description = models.TextField(verbose_name=_(u"Descrição"), max_length=500, blank=True)
    active = models.CharField(verbose_name=_(u"Exibir"), max_length=1, choices=CHOICE_ACTIVE, default='Y', blank=False)
    group = models.ForeignKey(verbose_name=_(u"Grupo de Usuário"), to=Group, null=True, blank=True)

    class Meta:
        ordering = ["-name"]
        db_table = "campotec_branch"
        verbose_name = _(u"Ramo")
        verbose_name_plural = _(u"Ramos")

    def __unicode__(self):
        return self.name

    def get_specialties_actives_order_by_name(self):
        return self.specialty_set.filter(active=ACTIVE).order_by('date','name')

    def get_specialties_actives_order_by_name_user(self, user):
        specialty_list = self.specialty_set.filter(active=ACTIVE).order_by('date','name')
        for specialty in specialty_list:
            specialty.check_inscribed(user)
        return specialty_list


class Specialty(CoreModel):
    """
    Especialidades
    """
    IMAGE_PATH = os.path.join('campotec', 'specialty')

    TURN_MORNING = 'M'
    TURN_AFTER = 'T'
    TURN_ALL_DAY = 'D'
    CHOICE_TURN = (
        (TURN_MORNING, _(u"Manhã")),
        (TURN_AFTER, _(u"Tarde")),
        (TURN_ALL_DAY, _(u"Manhã e Tarde")),
    )

    name = models.CharField(verbose_name=_(u"Nome"), max_length=100, null=False)
    description = models.TextField(verbose_name=_(u"Descrição"), max_length=500, blank=True)
    date = models.DateField(verbose_name=_(u"Data"))
    turn = models.CharField(verbose_name=_(u"Turno"), max_length=1, choices=CHOICE_TURN, default=TURN_ALL_DAY, blank=False)
    num_places = models.IntegerField(verbose_name=_(u"Nº de Vagas"), default=0, blank=False, null=False)
    inscription = models.ManyToManyField(to=User,db_table='campotec_specialty_inscription',blank=True)
    level_1 = models.BooleanField(verbose_name=_(u"Nível 1"), default=False)
    level_2 = models.BooleanField(verbose_name=_(u"Nível 2"), default=False)
    level_3 = models.BooleanField(verbose_name=_(u"Nível 3"), default=False)
    branch = models.ForeignKey(verbose_name=_(u"Ramo"), to=Branch, null=False)
    active = models.CharField(verbose_name=_(u"Exibir"), max_length=1, choices=CHOICE_ACTIVE, default=ACTIVE, blank=False)
    image = models.ImageField(verbose_name=_(u"Imagem"), upload_to=IMAGE_PATH, null=True, blank=True, help_text=_(u"Para não distorcer, envie uma imagem com resolução máxima de 200 x 200 px."))

    is_inscribed = False

    class Meta:
        ordering = ["-name", "-branch"]
        db_table = "campotec_specialty"
        verbose_name = _(u"Especialidade")
        verbose_name_plural = _(u"Especialidades")

    @staticmethod
    def remove_all_inscriptions_user(user):
        specialty_list = Specialty.objects.filter(inscription=user)
        for specialty in specialty_list:
            specialty.inscription.remove(user)

    def __unicode__(self):
        return self.name

    def check_inscribed(self, user=None):
        """
        Checa se o usuario esta inscrito na especialidade
        """
        if user in self.inscription.all():
            self.is_inscribed = True

    def get_image(self):
        if self.image:
            return "%s%s" % (settings.MEDIA_URL, self.image.name)
        else:
            return "%s/campotec/img/especialidade_padrao.jpg" % settings.STATIC_URL


class Programation(CoreModel):
    """
    Programação do Evento
    """
    IMAGE_PATH = os.path.join('campotec', 'programation')

    name = models.CharField(verbose_name=_(u"Nome"), max_length=100, null=False)
    date_time = models.DateTimeField(verbose_name=_(u"Data e Hora"))
    active = models.CharField(verbose_name=_(u"Exibir"), max_length=1, choices=CHOICE_ACTIVE, default='S', blank=False)
    description = models.TextField(verbose_name=_(u"Descrição"), max_length=500, blank=True)
    image = models.ImageField(verbose_name=_(u"Imagem"), upload_to=IMAGE_PATH, null=True, blank=True, help_text=_(u"Para não distorcer, envie uma imagem com resolução máxima de 200 x 200 px."))

    class Meta:
        ordering = ["-name", "-description"]
        db_table = "campotec_programation"
        verbose_name = _(u"Programação")
        verbose_name_plural = _(u"Programações")

    def __unicode__(self):
        return "%s - %s" % (self.name, self.date_time)


# class ImportInscriptions(CoreModel):
#
#     IMPORT_INSCRIPTION_FILE_PATH = os.path.join('campotec', 'import_inscription')
#
#     name = models.CharField(verbose_name=_(u"Nome"), max_length=100, blank=True, null=True)
#     file = models.FileField(verbose_name=_(u"Arquivo .XLS"), upload_to=IMPORT_INSCRIPTION_FILE_PATH, null=False, blank=False, help_text=_(u"Importe aqui o arquivo .xls com a lista de inscritos."))
#     branch = models.ForeignKey(verbose_name=_(u"Ramo"), to=Branch, null=False, help_text=_(u"Ramo ao qual pertencem os registros do arquivo .xls."))



@receiver(pre_delete, sender=Specialty)
@receiver(pre_delete, sender=Programation)
def delete_image(sender, instance, **kwargs):
    """
    Signal para deletar arquivo quando removido o registro.
    Passar False para o metodo delete para que a instancia não salve o model.
    Usado nos models:
    - Specialty
    - Programation
    """
    instance.image.delete(False)

@receiver(pre_save, sender=Specialty)
@receiver(pre_save, sender=Programation)
def delete_image_on_update(sender, instance, **kwargs):
    """
    Signal para deletar arquivo quando atualizado o registro.
    Passar False para o metodo delete para que a instancia não salve o model.
    Usado nos models:
    - Specialty
    - Programation
    """
    try:
        obj = Specialty.objects.get(id=instance.id)
        if not instance.image.name or (obj.image.file.name != instance.image.file.name):
            # Deleta a imagem
            obj.image.delete(save=False)
    except: pass

# -*- coding:utf-8 -*-
from copy import deepcopy
import os

from django.core.urlresolvers import reverse
from django.utils.html import strip_tags
from django.utils.safestring import mark_safe
from django.conf import settings

from django.utils.translation import ugettext_lazy as _
from django.db import models
from filebrowser.fields import FileBrowseField
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User, Group

from core.models import CoreModel, ACTIVE, INACTIVE, CHOICE_ACTIVE


class Event(CoreModel):
    """
    Evento
    """
    EVENT_IMAGE_PATH = "eventos/evento/"

    event_active = models.CharField(verbose_name=_(u"Ativar Evento"), max_length=1, choices=CHOICE_ACTIVE,
                                    default=ACTIVE, blank=False)
    event_title_menu = models.CharField(verbose_name=_(u"Título do Evento para o Menu"), max_length=255, blank=False,
                                        null=False, help_text=_(
            u"Título que vai no link à esquerda no Menu do Topo. Máximo 255 caracteres. Ex: Congresso"))
    event_description_short = models.CharField(verbose_name=_(u"Descrição curta"), max_length=255, blank=False,
                                               null=False, help_text=_(
            u"Descrição curta para Buscadores e Redes sociais. Ex: Congresso Escoteiro Regional 2015"))
    event_url = models.SlugField(verbose_name=_(u"Nome da URL do Evento"), unique=True, max_length=255, blank=False,
                                 null=False, help_text=_(u"Nome do link, ex: congresso-2015"))
    event_logo = FileBrowseField(verbose_name=_(u"Cabeçalho Logo"), directory=EVENT_IMAGE_PATH, max_length=200,
                                 blank=True, null=True, help_text=_(
            u"Para não distorcer e manter a responsividade, envie uma imagem com resolução de 300x300px."))
    event_title = RichTextField(verbose_name=_(u"Cabeçalho Título"), blank=True, config_name='description')
    event_image_background = FileBrowseField(verbose_name=_(u"Cabeçalho Imagem de Fundo"),
                                             directory=EVENT_IMAGE_PATH,
                                             max_length=200, blank=True, null=True, help_text=_(
            u"Para não distorcer, envie uma imagem com resolução máxima de 2362x591px."))
    event_social_image = FileBrowseField(verbose_name=_(u"Imagem para Redes Sociais"), directory=EVENT_IMAGE_PATH,
                                         max_length=200, blank=True, null=True, help_text=_(
            u"Imagem para exibir em links de Redes Sociais, como Facebook. Para imagem retangular envie em 600x315, para imagem quadrada envie em 200x200. Ou formatos maiores sempre mantendo a proporção."))
    information_active = models.CharField(verbose_name=_(u"Exibir Bloco Informações"), max_length=1,
                                          choices=CHOICE_ACTIVE, default=ACTIVE, blank=False)
    information_title = RichTextField(verbose_name=_(u"Informações Título"), config_name='title', null=True, blank=True)
    information_text = RichTextField(verbose_name=_(u"Informações Texto"), config_name='description', null=True,
                                     blank=True)

    local_active = models.CharField(verbose_name=_(u"Exibir Bloco Local"), max_length=1, choices=CHOICE_ACTIVE,
                                    default=ACTIVE, blank=False)
    local_maps_name = models.CharField(verbose_name=_(u"Local no Maps"), max_length=500, blank=True,
                                       help_text=_(u"Nome do Local no Google Maps."))
    local_title = RichTextField(verbose_name=_(u"Local Título"), config_name='title', null=True, blank=True)
    local_text = RichTextField(verbose_name=_(u"Local Texto"), blank=True, config_name='description')

    observation_active = models.CharField(verbose_name=_(u"Exibir Bloco Observações"), max_length=1,
                                          choices=CHOICE_ACTIVE, default=ACTIVE, blank=False)
    observation_title = RichTextField(verbose_name=_(u"Observações Título"), config_name='title', null=True, blank=True)
    observation_text = RichTextField(verbose_name=_(u"Observações Texto"), blank=True, config_name='description')

    list_events_active = models.CharField(verbose_name=_(u"Ativar Lista de Eventos"), max_length=1,
                                          choices=CHOICE_ACTIVE, default=ACTIVE, blank=False)
    list_events_title = RichTextField(verbose_name=_(u"Lista de Eventos Título"), config_name='title', null=True,
                                      blank=True)
    list_programations_active = models.CharField(verbose_name=_(u"Ativar Lista de Programações"), max_length=1,
                                                 choices=CHOICE_ACTIVE, default=ACTIVE, blank=False)
    list_programations_title = RichTextField(verbose_name=_(u"Lista de Programações Título"), config_name='title',
                                             null=True, blank=True)

    class Meta:
        ordering = ["event_active"]
        db_table = "event_homepage"
        verbose_name = _(u"Página de Evento")
        verbose_name_plural = _(u"Página de Eventos")

    def __unicode__(self):
        text = strip_tags(self.event_title)
        if len(text) > 50:
            text = "%s..." % text[0:50]
        else:
            text = "%s" % text
        return mark_safe(text)

    def get_absolute_url(self):
        """
        URL absoluta do Evento
        """
        return reverse('events:event-homepage', args=(self.event_url,))

    def get_url_preview(self):
        return reverse('events:event-preview', args=(self.event_url,))

    def get_link_preview(self):
        return '<a href="%s" target="_blank">%s</a>' % (
            reverse('events:event-preview', args=(self.event_url,)), unicode(_(u"Pré-visualizar")))

    def duplicate_save(self):
        obj_new = deepcopy(self)
        obj_new.id = None
        obj_new.event_title += "Cópia de %s" % (obj_new.event_title)
        obj_new.homepage_active = INACTIVE
        obj_new.save()
        return obj_new

    def is_information_active(self):
        if self.information_active == ACTIVE:
            return True
        else:
            return False

    def is_local_active(self):
        if self.local_active == ACTIVE:
            return True
        else:
            return False

    def is_observation_active(self):
        if self.observation_active == ACTIVE:
            return True
        else:
            return False

    def is_list_programations_active(self):
        if self.list_programations_active == ACTIVE:
            return True
        else:
            return False

    def get_event_logo(self):
        """
            retorna o caminho do logo do evento para montar a URL
        """
        if self.event_logo:
            return "%s/%s" % (settings.MEDIA_URL, self.event_logo)
        else:
            return False

    def get_event_image_background(self):
        if self.event_image_background:
            return "%s/%s" % (settings.MEDIA_URL, self.event_image_background)
        else:
            return os.path.join(settings.STATIC_URL, 'campotec', 'img', 'header.jpg')
# -*- coding:utf-8 -*-
from django.contrib.admin import helpers
from django.core.checks import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.utils.html import strip_tags
from django.utils.safestring import mark_safe

from django.utils.translation import ugettext_lazy as _
from django.contrib import admin
from django.core.urlresolvers import reverse
from django.conf import settings
from core.models import INACTIVE
from core.admin import activate, inactivate
from events.forms import EventForm
from events.models import Event, EventProgramation


class EventProgramationInline(admin.TabularInline):
    model = EventProgramation


class EventAdmin(admin.ModelAdmin):
    list_display = ('id', 'event_title_short', 'link_url_event_preview', 'event_active', 'information_active',
                    'local_active', 'observation_active')
    list_display_links = ('id', 'event_title_short', 'event_active',)
    actions = ('duplicate_item',)

    form = EventForm
    # inlines = [EventProgramationInline, ]

    def event_title_short(self, obj):
        """
        Retorna o titulo sem tags html para a exibição na listagem
        """
        return obj.__unicode__()
    event_title_short.allow_tags = True
    event_title_short.short_description = _(u"Título")

    def duplicate_item(self, request, queryset):
        if queryset.count() <> 1:
            self.message_user(request, _(u"Selecione apenas 1 item para duplicar"), level=messages.ERROR)
        else:
            obj = queryset.get()
            obj_new = obj.duplicate_save()
            return HttpResponseRedirect(redirect_to=reverse('admin:events_event_change', args=(obj_new.id,)))
    duplicate_item.short_description = _(u"Duplicar Item")


    def link_url_event_preview(self, obj):
        """
        Cria link para pre-visualizar a pagina
        """
        return obj.get_link_preview()

    link_url_event_preview.allow_tags = True
    link_url_event_preview.short_description = _(u"Pré-visualização")


class EventProgramationAdmin(admin.ModelAdmin):
    list_display = ('name', 'date_time', 'active', 'description_short', 'image_thumb')
    # list_display_links = ('name',)
    search_fields = ('name', 'description')
    ordering = ('date_time', 'name', 'active', 'description')
    list_filter = (
        ('active', admin.ChoicesFieldListFilter),
        'event',
    )
    actions = [inactivate, activate, ]

    def description_short(self, obj):
        """
        Corta o texto da Descrição para nao ficar exibir muito grande na listagem
        """
        text = strip_tags(obj.description)
        if (len(text) > 80):
            return "%s..." % text[0:80]
        else:
            return "%s" % text

    def image_thumb(self, obj):
        """
        Exibe miniatura da imagem na listagem
        """
        return '<img src="%s%s" style="width:50px;">' % (settings.MEDIA_URL, obj.image)

    image_thumb.allow_tags = True


admin.site.register(Event, EventAdmin)
admin.site.register(EventProgramation, EventProgramationAdmin)

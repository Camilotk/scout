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
from events.models import Event


class EventAdmin(admin.ModelAdmin):
    list_display = ('id', 'event_title_short', 'link_url_event_preview', 'event_active', 'information_active',
                    'local_active', 'observation_active')
    list_display_links = ('id', 'event_title_short', 'event_active',)
    actions = ('duplicate_item',)

    form = EventForm

    def event_title_short(self, obj):
        """
        Retorna o titulo sem tags html para a exibição na listagem
        """
        return obj.__unicode__()

    event_title_short.allow_tags = True

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


admin.site.register(Event, EventAdmin)

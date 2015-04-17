# -*- coding:utf-8 -*-
from django.template.defaultfilters import safe

from django.utils.translation import ugettext_lazy as _
from django import forms
from django.forms import ModelForm
from core.models import ACTIVE
from events.models import Event
from bootstrap_admin.widgets import LinkButton


class EventForm(ModelForm):
    """

    """
    btn_save_show_example = forms.CharField(label='', widget=LinkButton(label=_(u"Visualizar Página"),
                                                                        attrs={'class': 'btn btn-info',
                                                                               'target': '_blank',
                                                                               'disabled': 'disabled',
                                                                               'style': "width: auto;"}),
                                            help_text=_(u"Salve para Visualizar um página teste."), required=False)

    class Meta:
        model = Event
        fields = ['btn_save_show_example', 'event_active', 'event_title_menu', 'event_description_short', 'event_url',
                  'event_logo',
                  'event_title', 'event_image_background', 'event_social_image', 'information_active',
                  'information_title', 'information_text', 'local_active', 'local_maps_name', 'local_title',
                  'local_text', 'observation_active', 'observation_title', 'observation_text', 'list_events_active',
                  'list_events_title', 'list_programations_active', 'list_programations_title', ]

    def __init__(self, *args, **kwargs):
        super(EventForm, self).__init__(*args, **kwargs)

        instance = getattr(self, 'instance', None)
        if instance and instance.id:
            self.fields['btn_save_show_example'].widget.href = instance.get_url_preview()
            self.fields['btn_save_show_example'].widget.attrs.pop('disabled')
        else:
            self.fields['btn_save_show_example'].widget.attrs['disabled'] = 'disabled'

    def clean(self):
        # homepage_active = self.cleaned_data.get('homepage_active')
        # if homepage_active == ACTIVE and self.instance.has_more_one_active():
        # self.add_error('homepage_active', safe(_(u"Apenas um registro pode estar Ativo, deixe o campo <strong>Inativo</strong>.")))

        return self.cleaned_data
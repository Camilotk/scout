# -*- coding:utf-8 -*-
from django.template.defaultfilters import safe

from django.utils.translation import ugettext_lazy as _
from django import forms
from django.forms import ModelForm
from core.models import ACTIVE
from campotec.models import ImportInscriptions, Homepage
from bootstrap_admin.widgets import LinkButton


class ImportInscriptionsForm(ModelForm):
    class Meta:
        model = ImportInscriptions
        fields = ['name', 'file', 'branch']

    def clean(self):
        file = self.cleaned_data.get('file')
        branch = self.cleaned_data.get('branch')
        if file and branch:
            self.instance.import_users(file_read=file.read(), branch=branch)

        return self.cleaned_data


class HomepageForm(ModelForm):
    """

    """
    btn_save_show_example = forms.CharField(label='', widget=LinkButton(label=_(u"Visualizar Página"),
                                                                        attrs={'class': 'btn btn-info',
                                                                               'target': '_blank',
                                                                               'disabled': 'disabled',
                                                                               'style': "width: auto;"}),
                                            help_text=_(u"Salve para Visualizar um página teste."), required=False)

    class Meta:
        model = Homepage
        fields = ['homepage_active', 'btn_save_show_example', 'homepage_logo', 'homepage_title',
                  'homepage_image_background', 'information_active', 'information_title', 'information_text',
                  'local_active',
                  'local_maps_name', 'local_title', 'local_text', 'observation_active', 'observation_title',
                  'observation_text', ]

    def __init__(self, *args, **kwargs):
        super(HomepageForm, self).__init__(*args, **kwargs)

        instance = getattr(self, 'instance', None)
        if instance and instance.id:
            self.fields['btn_save_show_example'].widget.href = instance.get_url_homepage_preview()
            self.fields['btn_save_show_example'].widget.attrs.pop('disabled')
        else:
            self.fields['btn_save_show_example'].widget.attrs['disabled'] = 'disabled'

    def clean(self):
        homepage_active = self.cleaned_data.get('homepage_active')
        if homepage_active == ACTIVE and self.instance.has_more_one_active():
            self.add_error('homepage_active',
                           safe(_(u"Apenas um registro pode estar Ativo, deixe o campo <strong>Inativo</strong>.")))

        return self.cleaned_data
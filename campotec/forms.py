# -*- coding:utf-8 -*-

from django.forms import ModelForm
from campotec.models import ImportInscriptions


class ImportInscriptionsForm(ModelForm):

    class Meta:
        model = ImportInscriptions
        fields = ['name', 'file', 'branch']


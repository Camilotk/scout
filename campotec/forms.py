# -*- coding:utf-8 -*-

from django.forms import forms, ModelForm
from campotec.models import ImportInscriptions
import xlrd


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
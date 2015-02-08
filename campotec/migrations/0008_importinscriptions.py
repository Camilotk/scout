# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('campotec', '0007_auto_20150127_1548'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImportInscriptions',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100, null=True, verbose_name='Nome', blank=True)),
                ('file', models.FileField(help_text='Importe aqui o arquivo .xls com a lista de inscritos.', upload_to=b'campotec/import_inscription', verbose_name='Arquivo .XLS')),
                ('branch', models.ForeignKey(verbose_name='Ramo', to='campotec.Branch', help_text='Ramo ao qual pertencem os registros do arquivo .xls.')),
            ],
            options={
                'ordering': ['updated_at', '-__unicode__', '-file'],
                'db_table': 'campotec_import_inscription',
                'verbose_name': 'Importa\xe7\xe3o de Inscri\xe7\xf5es',
                'verbose_name_plural': 'Importa\xe7\xe3o de Inscri\xe7\xf5es',
            },
            bases=(models.Model,),
        ),
    ]

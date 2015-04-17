# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import filebrowser.fields
import ckeditor.fields


class Migration(migrations.Migration):
    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('event_active', models.CharField(default=b'Y', max_length=1, verbose_name='Ativar Evento',
                                                  choices=[(b'Y', 'Sim'), (b'N', 'N\xe3o')])),
                ('event_url', models.SlugField(help_text='Nome do link, ex: congresso-2015', max_length=255,
                                               verbose_name='Nome da URL do Evento')),
                ('event_logo', filebrowser.fields.FileBrowseField(
                    help_text='Para n\xe3o distorcer e manter a responsividade, envie uma imagem com resolu\xe7\xe3o de 300x300px.',
                    max_length=200, null=True, verbose_name='Cabe\xe7alho Logo', blank=True)),
                ('event_title', ckeditor.fields.RichTextField(verbose_name='Cabe\xe7alho T\xedtulo', blank=True)),
                ('event_image_background', filebrowser.fields.FileBrowseField(
                    help_text='Para n\xe3o distorcer, envie uma imagem com resolu\xe7\xe3o m\xe1xima de 2362x591px.',
                    max_length=200, null=True, verbose_name='Cabe\xe7alho Imagem de Fundo', blank=True)),
                ('information_active',
                 models.CharField(default=b'Y', max_length=1, verbose_name='Exibir Bloco Informa\xe7\xf5es',
                                  choices=[(b'Y', 'Sim'), (b'N', 'N\xe3o')])),
                ('information_title',
                 ckeditor.fields.RichTextField(null=True, verbose_name='Informa\xe7\xf5es T\xedtulo', blank=True)),
                ('information_text',
                 ckeditor.fields.RichTextField(null=True, verbose_name='Informa\xe7\xf5es Texto', blank=True)),
                ('local_active', models.CharField(default=b'Y', max_length=1, verbose_name='Exibir Bloco Local',
                                                  choices=[(b'Y', 'Sim'), (b'N', 'N\xe3o')])),
                ('local_maps_name', models.CharField(help_text='Nome do Local no Google Maps.', max_length=500,
                                                     verbose_name='Local no Maps', blank=True)),
                ('local_title', ckeditor.fields.RichTextField(null=True, verbose_name='Local T\xedtulo', blank=True)),
                ('local_text', ckeditor.fields.RichTextField(verbose_name='Local Texto', blank=True)),
                ('observation_active',
                 models.CharField(default=b'Y', max_length=1, verbose_name='Exibir Bloco Observa\xe7\xf5es',
                                  choices=[(b'Y', 'Sim'), (b'N', 'N\xe3o')])),
                ('observation_title',
                 ckeditor.fields.RichTextField(null=True, verbose_name='Observa\xe7\xf5es T\xedtulo', blank=True)),
                ('observation_text', ckeditor.fields.RichTextField(verbose_name='Observa\xe7\xf5es Texto', blank=True)),
                ('list_events_active',
                 models.CharField(default=b'Y', max_length=1, verbose_name='Ativar Lista de Eventos',
                                  choices=[(b'Y', 'Sim'), (b'N', 'N\xe3o')])),
                ('list_events_title',
                 ckeditor.fields.RichTextField(null=True, verbose_name='Lista de Eventos T\xedtulo', blank=True)),
                ('list_programations_active',
                 models.CharField(default=b'Y', max_length=1, verbose_name='Ativar Lista de Programa\xe7\xf5es',
                                  choices=[(b'Y', 'Sim'), (b'N', 'N\xe3o')])),
                ('list_programations_title',
                 ckeditor.fields.RichTextField(null=True, verbose_name='Lista de Programa\xe7\xf5es T\xedtulo',
                                               blank=True)),
            ],
            options={
                'ordering': ['event_active'],
                'db_table': 'event_homepage',
                'verbose_name': 'P\xe1gina Inicial',
                'verbose_name_plural': 'P\xe1ginas Iniciais',
            },
            bases=(models.Model,),
        ),
    ]

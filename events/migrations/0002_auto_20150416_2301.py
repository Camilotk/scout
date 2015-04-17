# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import filebrowser.fields


class Migration(migrations.Migration):
    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='event',
            options={'ordering': ['event_active'], 'verbose_name': 'P\xe1gina de Evento',
                     'verbose_name_plural': 'P\xe1gina de Eventos'},
        ),
        migrations.AddField(
            model_name='event',
            name='event_description_short',
            field=models.CharField(default='descri\xe7\xe3o',
                                   help_text='Descri\xe7\xe3o curta para Buscadores e Redes sociais. Ex: Congresso Escoteiro Regional 2015',
                                   max_length=255, verbose_name='Descri\xe7\xe3o curta'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='event',
            name='event_social_image',
            field=filebrowser.fields.FileBrowseField(
                help_text='Imagem para exibir em links de Redes Sociais, como Facebook. Para imagem retangular envie em 600x315, para imagem quadrada envie em 200x200. Ou formatos maiores sempre mantendo a propor\xe7\xe3o.',
                max_length=200, null=True, verbose_name='Imagem para Redes Sociais', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='event',
            name='event_title_menu',
            field=models.CharField(default='descri\xe7\xe3o',
                                   help_text='T\xedtulo que vai no link \xe0 esquerda no Menu do Topo. M\xe1ximo 255 caracteres. Ex: Congresso',
                                   max_length=255, verbose_name='T\xedtulo do Evento para o Menu'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='event',
            name='event_url',
            field=models.SlugField(help_text='Nome do link, ex: congresso-2015', unique=True, max_length=255,
                                   verbose_name='Nome da URL do Evento'),
            preserve_default=True,
        ),
    ]

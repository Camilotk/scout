# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import filebrowser.fields


class Migration(migrations.Migration):
    dependencies = [
        ('campotec', '0012_auto_20150215_1816'),
    ]

    operations = [
        migrations.AddField(
            model_name='specialty',
            name='active_inscription',
            field=models.BooleanField(default=True, verbose_name='Ativar Inscri\xe7\xe3o'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='specialty',
            name='show_num_inscriptions',
            field=models.BooleanField(default=True, verbose_name='Exibir N\xba de Inscritos'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='specialty',
            name='show_num_places',
            field=models.BooleanField(default=True, verbose_name='Exibir N\xba de Vagas'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='homepage',
            name='homepage_image_background',
            field=filebrowser.fields.FileBrowseField(
                help_text='Para n\xe3o distorcer, envie uma imagem com resolu\xe7\xe3o m\xe1xima de 2362x591px.',
                max_length=200, null=True, verbose_name='Cabe\xe7alho Imagem de Fundo', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='homepage',
            name='homepage_logo',
            field=filebrowser.fields.FileBrowseField(
                help_text='Para n\xe3o distorcer e manter a responsividade, envie uma imagem com resolu\xe7\xe3o de 300x300px.',
                max_length=200, null=True, verbose_name='Cabe\xe7alho Logo', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='programation',
            name='image',
            field=filebrowser.fields.FileBrowseField(
                help_text='Para n\xe3o distorcer, envie uma imagem com resolu\xe7\xe3o m\xe1xima de 200x200 px.',
                max_length=200, null=True, verbose_name='Imagem', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='specialty',
            name='image',
            field=filebrowser.fields.FileBrowseField(
                help_text='Para n\xe3o distorcer, envie uma imagem com resolu\xe7\xe3o m\xe1xima de 200x200 px.',
                max_length=200, null=True, verbose_name='Imagem', blank=True),
            preserve_default=True,
        ),
    ]

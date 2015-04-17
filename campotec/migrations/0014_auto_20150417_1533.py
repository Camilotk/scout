# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):
    dependencies = [
        ('campotec', '0013_auto_20150325_2348'),
    ]

    operations = [
        migrations.AlterField(
            model_name='specialty',
            name='active_inscription',
            field=models.BooleanField(default=True,
                                      help_text='Ativa a inscri\xe7\xe3o na especialidade, se marcado exibe o bot\xe3o para inscri\xe7\xe3o.',
                                      verbose_name='Ativar Inscri\xe7\xe3o'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='specialty',
            name='inscription',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL, db_table=b'campotec_specialty_inscription',
                                         verbose_name='Inscri\xe7\xf5es', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='specialty',
            name='show_num_inscriptions',
            field=models.BooleanField(default=True,
                                      help_text='Se marcado sempre exibe a quantidade de inscritos na especialidade.',
                                      verbose_name='Exibir N\xba de Inscritos'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='specialty',
            name='show_num_places',
            field=models.BooleanField(default=True,
                                      help_text='Se marcado sempre exibe o N\xfamero de Vagas da especialidade.',
                                      verbose_name='Exibir N\xba de Vagas'),
            preserve_default=True,
        ),
    ]

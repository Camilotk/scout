# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0002_registrationprofile_scout_group'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='registrationprofile',
            options={'verbose_name': 'Perfil', 'verbose_name_plural': 'Perfis'},
        ),
        migrations.AlterField(
            model_name='registrationprofile',
            name='activation_key',
            field=models.CharField(max_length=40, verbose_name='Chave de Ativa\xe7\xe3o'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='registrationprofile',
            name='scout_group',
            field=models.ForeignKey(verbose_name='Grupo Escoteiro', blank=True, to='scout_group.ScoutGroup', null=True),
            preserve_default=True,
        ),
    ]

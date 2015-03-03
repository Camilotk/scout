# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('campotec', '0011_homepage'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='homepage',
            options={'ordering': ['homepage_active'], 'verbose_name': 'P\xe1gina Inicial', 'verbose_name_plural': 'P\xe1ginas Iniciais'},
        ),
        migrations.AddField(
            model_name='homepage',
            name='local_maps_name',
            field=models.CharField(default=datetime.datetime(2015, 2, 15, 18, 16, 53, 390496), help_text='Nome do Local no Google Maps.', max_length=500, verbose_name='Local no Maps', blank=True),
            preserve_default=False,
        ),
    ]

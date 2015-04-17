# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):
    dependencies = [
        ('events', '0003_eventprogramation'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='event',
            options={'ordering': ['event_active'], 'verbose_name': 'Evento', 'verbose_name_plural': 'Eventos'},
        ),
        migrations.AddField(
            model_name='eventprogramation',
            name='event',
            field=models.ForeignKey(blank=True, to='events.Event',
                                    help_text='Selecione o Evento desta Programa\xe7\xe3o.', null=True),
            preserve_default=True,
        ),
    ]

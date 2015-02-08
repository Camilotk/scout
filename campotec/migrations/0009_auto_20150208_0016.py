# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('campotec', '0008_importinscriptions'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='importinscriptions',
            options={'ordering': ['updated_at', '-name', '-file'], 'verbose_name': 'Importa\xe7\xe3o de Inscri\xe7\xf5es', 'verbose_name_plural': 'Importa\xe7\xe3o de Inscri\xe7\xf5es'},
        ),
    ]

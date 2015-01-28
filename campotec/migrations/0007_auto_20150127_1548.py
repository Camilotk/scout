# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.datetime_safe


class Migration(migrations.Migration):

    dependencies = [
        ('campotec', '0006_auto_20150125_1833'),
    ]

    operations = [
        migrations.AddField(
            model_name='specialty',
            name='date',
            field=models.DateField(default=django.utils.datetime_safe.datetime.now, verbose_name='Data'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='specialty',
            name='turn',
            field=models.CharField(default=b'D', max_length=1, verbose_name='Turno', choices=[(b'M', 'Manh\xe3'), (b'T', 'Tarde'), (b'D', 'Manh\xe3 e Tarde')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='specialty',
            name='active',
            field=models.CharField(default=b'Y', max_length=1, verbose_name='Exibir', choices=[(b'Y', 'Sim'), (b'N', 'N\xe3o')]),
            preserve_default=True,
        ),
    ]

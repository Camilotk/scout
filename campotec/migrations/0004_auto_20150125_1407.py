# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('campotec', '0003_auto_20150125_1356'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='programation',
            options={'ordering': ['-name', '-description'], 'verbose_name': 'Programa\xe7\xe3o', 'verbose_name_plural': 'Programa\xe7\xf5es'},
        ),
        migrations.AddField(
            model_name='programation',
            name='active',
            field=models.CharField(default=b'S', max_length=1, verbose_name='Exibir', choices=[(b'Y', 'Sim'), (b'N', 'N\xe3o')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='programation',
            name='image',
            field=models.ImageField(help_text='Para n\xe3o distorcer, envie uma imagem com resolu\xe7\xe3o m\xe1xima de 200 x 200 px.', upload_to=b'campotec/programation', null=True, verbose_name='Imagem', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='specialty',
            name='image',
            field=models.ImageField(help_text='Para n\xe3o distorcer, envie uma imagem com resolu\xe7\xe3o m\xe1xima de 200 x 200 px.', upload_to=b'campotec/specialty', null=True, verbose_name='Imagem', blank=True),
            preserve_default=True,
        ),
        migrations.AlterModelTable(
            name='programation',
            table='campotec_programation',
        ),
    ]

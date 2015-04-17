# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import filebrowser.fields
import ckeditor.fields


class Migration(migrations.Migration):
    dependencies = [
        ('events', '0002_auto_20150416_2301'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventProgramation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100, verbose_name='Nome')),
                ('image', filebrowser.fields.FileBrowseField(
                    help_text='Para n\xe3o distorcer, envie uma imagem com resolu\xe7\xe3o m\xe1xima de 200x200px.',
                    max_length=200, null=True, verbose_name='Imagem', blank=True)),
                ('date_time', models.DateTimeField(verbose_name='Data e Hora')),
                ('active', models.CharField(default=b'S', max_length=1, verbose_name='Exibir',
                                            choices=[(b'Y', 'Sim'), (b'N', 'N\xe3o')])),
                ('description',
                 ckeditor.fields.RichTextField(max_length=1000, verbose_name='Descri\xe7\xe3o', blank=True)),
            ],
            options={
                'ordering': ['-name', '-description'],
                'db_table': 'event_programation',
                'verbose_name': 'Programa\xe7\xe3o',
                'verbose_name_plural': 'Programa\xe7\xf5es',
            },
            bases=(models.Model,),
        ),
    ]

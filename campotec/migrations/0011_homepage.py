# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('campotec', '0010_auto_20150210_1434'),
    ]

    operations = [
        migrations.CreateModel(
            name='Homepage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('homepage_active', models.CharField(default=b'Y', max_length=1, verbose_name='Ativar P\xe1gina Inicial', choices=[(b'Y', 'Sim'), (b'N', 'N\xe3o')])),
                ('homepage_logo', models.ImageField(help_text='Para n\xe3o distorcer e manter a responsividade, envie uma imagem com resolu\xe7\xe3o m\xe9dia de 300 x 300px.', upload_to=b'campotec/homepage', null=True, verbose_name='Cabe\xe7alho Logo', blank=True)),
                ('homepage_title', ckeditor.fields.RichTextField(verbose_name='Cabe\xe7alho T\xedtulo', blank=True)),
                ('homepage_image_background', models.ImageField(help_text='Para n\xe3o distorcer, envie uma imagem com resolu\xe7\xe3o m\xe1xima de 200 x 200 px.', upload_to=b'campotec/homepage', null=True, verbose_name='Cabe\xe7alho Imagem de Fundo', blank=True)),
                ('information_active', models.CharField(default=b'Y', max_length=1, verbose_name='Exibir Bloco Informa\xe7\xf5es', choices=[(b'Y', 'Sim'), (b'N', 'N\xe3o')])),
                ('information_title', ckeditor.fields.RichTextField(null=True, verbose_name='Informa\xe7\xf5es T\xedtulo', blank=True)),
                ('information_text', ckeditor.fields.RichTextField(null=True, verbose_name='Informa\xe7\xf5es Texto', blank=True)),
                ('local_active', models.CharField(default=b'Y', max_length=1, verbose_name='Exibir Bloco Local', choices=[(b'Y', 'Sim'), (b'N', 'N\xe3o')])),
                ('local_title', ckeditor.fields.RichTextField(null=True, verbose_name='Local T\xedtulo', blank=True)),
                ('local_text', ckeditor.fields.RichTextField(verbose_name='Local Texto', blank=True)),
                ('observation_active', models.CharField(default=b'Y', max_length=1, verbose_name='Exibir Bloco Observa\xe7\xf5es', choices=[(b'Y', 'Sim'), (b'N', 'N\xe3o')])),
                ('observation_title', ckeditor.fields.RichTextField(null=True, verbose_name='Observa\xe7\xf5es T\xedtulo', blank=True)),
                ('observation_text', ckeditor.fields.RichTextField(verbose_name='Observa\xe7\xf5es Texto', blank=True)),
            ],
            options={
                'db_table': 'campotec_homepage',
            },
            bases=(models.Model,),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('campotec', '0002_specialty_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Programation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100, verbose_name='Nome')),
                ('description', models.TextField(max_length=500, verbose_name='Descri\xe7\xe3o', blank=True)),
                ('date_time', models.DateTimeField(verbose_name='Data e Hora')),
                ('image', models.ImageField(help_text='Para n\xe3o distorcer, envie uma imagem com resolu\xe7\xe3o m\xe1xima de 200 x 200 px.', upload_to=b'campotec/programation', null=True, verbose_name='Imagem')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='branch',
            name='active',
            field=models.CharField(default=b'Y', max_length=1, verbose_name='Exibir', choices=[(b'Y', 'Sim'), (b'N', 'N\xe3o')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='specialty',
            name='image',
            field=models.ImageField(help_text='Para n\xe3o distorcer, envie uma imagem com resolu\xe7\xe3o m\xe1xima de 200 x 200 px.', upload_to=b'campotec/specialty', null=True, verbose_name='Imagem'),
            preserve_default=True,
        ),
    ]

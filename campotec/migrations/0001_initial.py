# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100, verbose_name='Nome')),
                ('description', models.TextField(max_length=500, verbose_name='Descri\xe7\xe3o', blank=True)),
                ('active', models.CharField(default=b'S', max_length=1, verbose_name='Exibir', choices=[(b'Y', 'Sim'), (b'N', 'N\xe3o')])),
            ],
            options={
                'ordering': ['-name'],
                'db_table': 'campotec_branch',
                'verbose_name': 'Ramo',
                'verbose_name_plural': 'Ramos',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Specialty',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100, verbose_name='Nome')),
                ('description', models.TextField(max_length=500, verbose_name='Descri\xe7\xe3o', blank=True)),
                ('level_1', models.BooleanField(default=False, verbose_name='N\xedvel 1')),
                ('level_2', models.BooleanField(default=False, verbose_name='N\xedvel 2')),
                ('level_3', models.BooleanField(default=False, verbose_name='N\xedvel 3')),
                ('active', models.CharField(default=b'S', max_length=1, verbose_name='Exibir', choices=[(b'Y', 'Sim'), (b'N', 'N\xe3o')])),
                ('branch', models.ForeignKey(verbose_name='Ramo', to='campotec.Branch')),
            ],
            options={
                'ordering': ['-name', '-branch'],
                'db_table': 'campotec_specialty',
                'verbose_name': 'Especialidade',
                'verbose_name_plural': 'Especialidades',
            },
            bases=(models.Model,),
        ),
    ]

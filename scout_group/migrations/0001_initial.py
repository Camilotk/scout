# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ScoutGroup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100, null=True, verbose_name='Nome', blank=True)),
                ('number', models.IntegerField(verbose_name='Numeral')),
                ('uf', models.CharField(default=b'RS', help_text='Estado do Grupo Escoteiro.', max_length=2, verbose_name='UF', choices=[(b'RS', 'Rio Grande do Sul'), (b'AC', 'Acre'), (b'AL', 'Alagoas'), (b'AP', 'Amap\xe1'), (b'AM', 'Amazonas'), (b'BA', 'Bahia'), (b'CE', 'Cear\xe1'), (b'DF', 'Distrito Federal'), (b'ES', 'Esp\xedrito Santo'), (b'GO', 'Goi\xe1s'), (b'MA', 'Maranh\xe3o'), (b'MT', 'Mato Grosso'), (b'MS', 'Mato Grosso do Sul'), (b'MG', 'Minas Gerais'), (b'PA', 'Par\xe1'), (b'PB', 'Para\xedba'), (b'PR', 'Paran\xe1'), (b'PE', 'Pernambuco'), (b'PI', 'Piau\xed'), (b'RJ', 'Rio de Janeiro'), (b'RN', 'Rio Grande do Norte'), (b'RO', 'Rond\xf4nia'), (b'RR', 'Roraima'), (b'SC', 'Santa Catarina'), (b'SP', 'S\xe3o Paulo'), (b'SE', 'Sergipe'), (b'TO', 'Tocantins')])),
                ('active', models.CharField(default=b'Y', max_length=1, verbose_name='Exibir', choices=[(b'Y', 'Sim'), (b'N', 'N\xe3o')])),
            ],
            options={
                'ordering': ['-name'],
                'db_table': 'scout_group',
                'verbose_name': 'Grupo Escoteiro',
                'verbose_name_plural': 'Grupos Escoteiros',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserScoutGroup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('scout_group', models.ForeignKey(to='scout_group.ScoutGroup')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, unique=True)),
            ],
            options={
                'ordering': ['user', 'scout_group'],
                'db_table': 'scout_group_userscoutgroup',
                'verbose_name': 'Usu\xe1rio por Grupo Escoteiro',
                'verbose_name_plural': 'Usu\xe1rios por Grupo Escoteiro',
            },
            bases=(models.Model,),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0001_initial'),
        ('campotec', '0004_auto_20150125_1407'),
    ]

    operations = [
        migrations.AddField(
            model_name='branch',
            name='group',
            field=models.ForeignKey(verbose_name='Grupo de Usu\xe1rio', blank=True, to='auth.Group', null=True),
            preserve_default=True,
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('campotec', '0005_branch_group'),
    ]

    operations = [
        migrations.AddField(
            model_name='specialty',
            name='inscription',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL, db_table=b'campotec_specialty_inscription', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='specialty',
            name='num_places',
            field=models.IntegerField(default=0, verbose_name='N\xba de Vagas'),
            preserve_default=True,
        ),
    ]

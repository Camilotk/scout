# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('campotec', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='specialty',
            name='image',
            field=models.ImageField(upload_to=b'/home/guerra/git/scout/media/campotec', null=True, verbose_name='Banner'),
            preserve_default=True,
        ),
    ]

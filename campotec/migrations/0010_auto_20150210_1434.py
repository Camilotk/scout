# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('campotec', '0009_auto_20150208_0016'),
    ]

    operations = [
        migrations.AlterField(
            model_name='programation',
            name='description',
            field=ckeditor.fields.RichTextField(max_length=1000, verbose_name='Descri\xe7\xe3o', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='specialty',
            name='description',
            field=ckeditor.fields.RichTextField(max_length=1000, verbose_name='Descri\xe7\xe3o', blank=True),
            preserve_default=True,
        ),
    ]

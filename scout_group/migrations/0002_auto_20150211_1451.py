# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scout_group', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userscoutgroup',
            name='scout_group',
        ),
        migrations.RemoveField(
            model_name='userscoutgroup',
            name='user',
        ),
        migrations.DeleteModel(
            name='UserScoutGroup',
        ),
    ]

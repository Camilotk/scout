# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scout_group', '0002_auto_20150211_1451'),
        ('registration', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='registrationprofile',
            name='scout_group',
            field=models.ForeignKey(to='scout_group.ScoutGroup', null=True),
            preserve_default=True,
        ),
    ]

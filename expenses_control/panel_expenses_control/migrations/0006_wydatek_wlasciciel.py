# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('panel_expenses_control', '0005_auto_20151216_1246'),
    ]

    operations = [
        migrations.AddField(
            model_name='wydatek',
            name='wlasciciel',
            field=models.ForeignKey(default=1, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]

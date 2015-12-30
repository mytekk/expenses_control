# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('panel_expenses_control', '0004_auto_20151029_1301'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wydatek',
            name='notatka',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='wydatek',
            name='podkategoria',
            field=models.ForeignKey(to='panel_expenses_control.Podkategoria', null=True),
        ),
    ]

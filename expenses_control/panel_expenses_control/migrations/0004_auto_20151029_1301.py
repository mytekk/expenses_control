# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('panel_expenses_control', '0003_auto_20151028_1123'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='podkategoria',
            options={'ordering': ['kategoria'], 'verbose_name_plural': 'Podkategorie'},
        ),
    ]

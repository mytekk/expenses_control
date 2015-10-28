# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('panel_expenses_control', '0002_wydatek'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='kategoria',
            options={'ordering': ['nazwa'], 'verbose_name_plural': 'Kategorie'},
        ),
        migrations.AlterModelOptions(
            name='kontrahent',
            options={'ordering': ['nazwa'], 'verbose_name_plural': 'Kontrahenci'},
        ),
        migrations.AlterModelOptions(
            name='osoba',
            options={'ordering': ['nazwa'], 'verbose_name_plural': 'Osoby'},
        ),
        migrations.AlterModelOptions(
            name='podkategoria',
            options={'ordering': ['nazwa'], 'verbose_name_plural': 'Podkategorie'},
        ),
        migrations.AlterModelOptions(
            name='wydatek',
            options={'verbose_name_plural': 'Wydatki'},
        ),
        migrations.AlterModelOptions(
            name='zrodlo',
            options={'ordering': ['nazwa'], 'verbose_name_plural': 'Zrodla'},
        ),
        migrations.RenameField(
            model_name='kategoria',
            old_name='name',
            new_name='nazwa',
        ),
        migrations.RenameField(
            model_name='kontrahent',
            old_name='name',
            new_name='nazwa',
        ),
        migrations.RenameField(
            model_name='osoba',
            old_name='name',
            new_name='nazwa',
        ),
        migrations.RenameField(
            model_name='podkategoria',
            old_name='name',
            new_name='nazwa',
        ),
        migrations.RenameField(
            model_name='zrodlo',
            old_name='name',
            new_name='nazwa',
        ),
    ]

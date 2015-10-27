# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('panel_expenses_control', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Wydatek',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('data', models.DateField()),
                ('kwota', models.DecimalField(max_digits=7, decimal_places=2)),
                ('notatka', models.CharField(max_length=200)),
                ('kategoria', models.ForeignKey(to='panel_expenses_control.Kategoria')),
                ('kontrahent', models.ForeignKey(to='panel_expenses_control.Kontrahent')),
                ('osoba', models.ForeignKey(to='panel_expenses_control.Osoba')),
                ('podkategoria', models.ForeignKey(to='panel_expenses_control.Podkategoria')),
                ('zrodlo', models.ForeignKey(to='panel_expenses_control.Zrodlo')),
            ],
        ),
    ]

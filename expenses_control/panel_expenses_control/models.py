from django.db import models
from datetime import datetime
from django.utils.timezone import *

class Kontrahent(models.Model):
	nazwa = models.CharField(max_length=100)

        def __unicode__(self):
                return self.nazwa

        class Meta:
                verbose_name_plural = u"Kontrahenci"
                ordering = ['nazwa']

class Osoba(models.Model):
        nazwa = models.CharField(max_length=100)

        def __unicode__(self):
                return self.nazwa

        class Meta:
                verbose_name_plural = u"Osoby"
                ordering = ['nazwa']

class Zrodlo(models.Model):
        nazwa = models.CharField(max_length=100)

        def __unicode__(self):
                return self.nazwa

        class Meta:
                verbose_name_plural = u"Zrodla"
                ordering = ['nazwa']

class Kategoria(models.Model):
        nazwa = models.CharField(max_length=100)

        def __unicode__(self):
                return self.nazwa

        class Meta:
                verbose_name_plural = u"Kategorie"
                ordering = ['nazwa']

class Podkategoria(models.Model):
	kategoria = models.ForeignKey('Kategoria')
        nazwa = models.CharField(max_length=100)

        def __unicode__(self):
                return self.nazwa

        class Meta:
                verbose_name_plural = u"Podkategorie"
                ordering = ['nazwa']

class Wydatek(models.Model):
	zrodlo = models.ForeignKey('Zrodlo')
	data = models.DateField(auto_now=False, auto_now_add=False)
	kontrahent = models.ForeignKey('Kontrahent')
	kwota = models.DecimalField(max_digits=7, decimal_places=2)
        kategoria = models.ForeignKey('Kategoria')
	podkategoria = models.ForeignKey('Podkategoria')
	osoba = models.ForeignKey('Osoba')
        notatka = models.CharField(max_length=200)

	class Meta:
                verbose_name_plural = u"Wydatki"

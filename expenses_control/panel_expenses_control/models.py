from django.db import models
from datetime import datetime

class Kontrahent(models.Model):
	name = models.CharField(max_length=100)

class Osoba(models.Model):
        name = models.CharField(max_length=100)

class Zrodlo(models.Model):
        name = models.CharField(max_length=100)

class Kategoria(models.Model):
        name = models.CharField(max_length=100)

class Podkategoria(models.Model):
	kategoria = models.ForeignKey('Kategoria')
        name = models.CharField(max_length=100)

class Wydatek(models.Model):
	zrodlo = models.ForeignKey('Zrodlo')
	data = models.DateField(auto_now=False, auto_now_add=False)
	kontrahent = models.ForeignKey('Kontrahent')
	kwota = models.DecimalField(max_digits=7, decimal_places=2)
        kategoria = models.ForeignKey('Kategoria')
	podkategoria = models.ForeignKey('Podkategoria')
	osoba = models.ForeignKey('Osoba')
        notatka = models.CharField(max_length=200)

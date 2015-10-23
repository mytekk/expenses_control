from django.db import models

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

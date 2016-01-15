#coding: utf-8

from django import forms
from .models  import *

class formularz_nowego_wpisu(forms.Form):
        zrodlo = forms.ModelChoiceField(label=u"Źródło finansowania:", queryset=Zrodlo.objects.all(), widget=forms.RadioSelect(), empty_label=None) 
        data = forms.DateField()
        kontrahent = forms.ModelChoiceField(label="Kontrahent:", queryset=Kontrahent.objects.all(), empty_label=u"Wybierz wartość")
        kwota = forms.DecimalField(min_value=0.01)
        kategoria = forms.ModelChoiceField(label="Kategoria:", queryset=Kategoria.objects.all(), empty_label=u"Wybierz wartość")
        podkategoria = forms.ModelChoiceField(label="Podkategoria:", queryset=Podkategoria.objects.all(), required=False, empty_label=u"-- brak --")
        osoba = forms.ModelChoiceField(label="Dotyczy osoby:", queryset=Osoba.objects.all(), empty_label=u"Wybierz wartość")
        notatka = forms.CharField(label='Notatka:', max_length=100, required=False)
	wlasciciel = forms.IntegerField()

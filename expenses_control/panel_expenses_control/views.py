#coding: utf-8

from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from .models  import *
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
import calendar
import locale
import datetime

def month_name(month_number):
	locale.setlocale(locale.LC_ALL, 'pl_PL.utf-8')
	return calendar.month_name[month_number]

def index(request, rok=None, miesiac=None):
	if not request.user.is_authenticated():
		powrotny_url = reverse('django.contrib.auth.views.login')
		return HttpResponseRedirect(powrotny_url)

	lista_miesiecy = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

	if rok is None:
		rok = datetime.datetime.now().year

	if miesiac is None:
		miesiac = datetime.datetime.now().month

	if int(miesiac) not in lista_miesiecy:
		rok = datetime.datetime.now().year
                miesiac = datetime.datetime.now().month

	miesiac_nazwa = month_name(int(miesiac))

	lista_kategorii = Kategoria.objects.all()

	lista_par_miesiac_rok = [(rekord.data.year, rekord.data.month) for rekord in Wydatek.objects.all()]
	lista_par_miesiac_rok = list(set(lista_par_miesiac_rok))
	lista_par_miesiac_rok = sorted(lista_par_miesiac_rok, reverse=True)

	template = loader.get_template('panel_expenses_control/index.html')
	slownik = {'lista_kategorii': lista_kategorii, 'lista_par_miesiac_rok' : lista_par_miesiac_rok, 'rok' : rok, 'miesiac' : miesiac, 'miesiac_nazwa' : miesiac_nazwa,}
	context = RequestContext(request, slownik)
	return HttpResponse(template.render(context))

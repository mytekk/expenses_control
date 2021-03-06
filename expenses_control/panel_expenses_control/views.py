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
from django.db.models import Sum, Count
from .forms import formularz_nowego_wpisu
from django.contrib import messages
from django.contrib.auth.models import User

# funkcja pomocnicza
def polish_month_name(month_number):
	locale.setlocale(locale.LC_ALL, 'pl_PL.UTF-8')
	return calendar.month_name[month_number]

# funkcja pomocnicza
def daj_liste_par_miesiac_rok(user_id):
	lista_par_miesiac_rok = [(rekord.data.year, rekord.data.month, polish_month_name(rekord.data.month)) for rekord in Wydatek.objects.filter(wlasciciel=user_id)]
	lista_par_miesiac_rok = list(set(lista_par_miesiac_rok))
	lista_par_miesiac_rok = sorted(lista_par_miesiac_rok, reverse=True)
	return lista_par_miesiac_rok

# pomocnicza funkcja wykorzystywana na stronie z formularzem, podczas zdarzenia 'change' na liście kategorii
def podaj_podkategorie(request, kat_id):
        from django.core import serializers
        json_podkat = serializers.serialize("json", Podkategoria.objects.filter(kategoria = kat_id))
        return HttpResponse(json_podkat, content_type="application/javascript")

# główna strona z wydatkami
def index(request, rok=None, miesiac=None):
	if not request.user.is_authenticated():
		powrotny_url = reverse('django.contrib.auth.views.login')
		return HttpResponseRedirect(powrotny_url)

	user = request.user

	lista_miesiecy = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

	# gdy nie przekazano roku i miesiąca w argumencie
	if rok is None:
		rok = datetime.datetime.now().year
	if miesiac is None:
		miesiac = datetime.datetime.now().month

	# sprawdzam poprawność przekazanego w argumencie (lub ustalonego powyżej) numeru miesiąca
	if int(miesiac) not in lista_miesiecy:
		rok = datetime.datetime.now().year
                miesiac = datetime.datetime.now().month

	miesiac_nazwa = polish_month_name(int(miesiac))

	lista_kategorii = Kategoria.objects.all()

	wydatki = Wydatek.objects.filter(data__year=rok, data__month=miesiac, wlasciciel=user.pk).order_by('data')

	# podstawowe statystyki
	suma_wszystkich_wydatkow = Wydatek.objects.filter(data__year=rok, data__month=miesiac, wlasciciel=user.pk).aggregate(suma_miesieczna=Sum('kwota'))
	licznik_wszystkich_wydatkow = Wydatek.objects.filter(data__year=rok, data__month=miesiac, wlasciciel=user.pk).aggregate(licznik_miesieczny=Count('kwota'))
	suma_per_kategoria = Wydatek.objects.filter(data__year=rok, data__month=miesiac, wlasciciel=user.pk).values('kategoria', 'kategoria__nazwa').annotate(suma_w_kategorii=Sum('kwota')).order_by('kategoria__nazwa')
	suma_per_podkategoria = Wydatek.objects.filter(data__year=rok, data__month=miesiac, wlasciciel=user.pk).values('podkategoria', 'podkategoria__nazwa', 'kategoria', 'kategoria__nazwa').annotate(suma_w_podkategorii=Sum('kwota')).order_by('podkategoria__nazwa')
	suma_per_osoba = Wydatek.objects.filter(data__year=rok, data__month=miesiac, wlasciciel=user.pk).values('osoba', 'osoba__nazwa').annotate(suma_na_osobe=Sum('kwota')).order_by('-suma_na_osobe')
	suma_per_kontrahent = Wydatek.objects.filter(data__year=rok, data__month=miesiac, wlasciciel=user.pk).values('kontrahent', 'kontrahent__nazwa').annotate(suma_na_kontrahenta=Sum('kwota')).order_by('-suma_na_kontrahenta')
	licznik_per_kontrahent = Wydatek.objects.filter(data__year=rok, data__month=miesiac, wlasciciel=user.pk).values('kontrahent', 'kontrahent__nazwa').annotate(licznik_na_kontrahenta=Count('kwota')).order_by('-licznik_na_kontrahenta')

	# ustalam listę par rok-miesiac dla danego użytkownika
	lista_par_miesiac_rok = daj_liste_par_miesiac_rok(user.pk)

	# przygotowanie do wyświetlenia strony
	template = loader.get_template('panel_expenses_control/index.html')
	slownik = {'lista_kategorii': lista_kategorii, 'lista_par_miesiac_rok' : lista_par_miesiac_rok, 'rok' : rok, 'miesiac' : miesiac, 'miesiac_nazwa' : miesiac_nazwa, 'wydatki':wydatki, 'suma_wszystkich_wydatkow':suma_wszystkich_wydatkow, 'licznik_wszystkich_wydatkow':licznik_wszystkich_wydatkow, 'suma_per_kategoria':suma_per_kategoria, 'suma_per_podkategoria':suma_per_podkategoria, 'suma_per_osoba':suma_per_osoba, 'suma_per_kontrahent':suma_per_kontrahent, 'licznik_per_kontrahent':licznik_per_kontrahent}
	context = RequestContext(request, slownik)
	return HttpResponse(template.render(context))

def nowywydatek(request):
        if not request.user.is_authenticated():
                powrotny_url = reverse('django.contrib.auth.views.login')
                return HttpResponseRedirect(powrotny_url)

	user = request.user

	flaga = "jeszcze nic nie wiem"

	# if this is a POST request we need to process the form data
	if request.method == 'POST':	
		# create a form instance and populate it with data from the request:
		form = formularz_nowego_wpisu(request.POST)

		# check whether it's valid:
		if form.is_valid():
			# process the data in form.cleaned_data as required
			nowy_wydatek = Wydatek(zrodlo=form.cleaned_data['zrodlo'],
					data = form.cleaned_data['data'],
					kontrahent = form.cleaned_data['kontrahent'],
					kwota = form.cleaned_data['kwota'],
					kategoria = form.cleaned_data['kategoria'],
					podkategoria = form.cleaned_data['podkategoria'],
					osoba = form.cleaned_data['osoba'],
					notatka = form.cleaned_data['notatka'],
					wlasciciel = user
					)

			# próba zapisu do bazy
			try:
				nowy_wydatek.save()
				messages.success(request, 'Poprawnie dodano nowy rekord.')

			except:

				messages.error(request, 'Wystąpił błąd podczas próby zapisu.')

			# po próbie zapisu powracam do strony z formularzem, czyli tej samej strony
			return HttpResponseRedirect('nowywydatek')
		#else:
			#czyli jesli wyslano bledy formularz, to w tym miejscu nie robię nic, bo nie muszę.
	       		# Chcę wyświetlić formularz jeszcze raz, zeby nie tracic tych pol, ktore byly dobrze wpisane
			# osiągam to poprzez to, że w tym miejscu kodu gdzie teraz czytasz posiadam zmienną 'form' z czesciowo
	       		# dobrymi danymi. Nie przechodzę do poniżeszego else (bo cały czas jestem w czesci POST od głównego if'a),
			# czyli po opuszczeniu głównego if'a przechodzę do przygotowania do wyswietlenia strony, a w slowniku
			# znajdzie się właśnie ten mój formularz utworzony w tym miejscu.

			# if a GET (or any other method) we'll create a blank form
	else:
		# domyślnie dla wydatku przewiduję dzisiejszą datę
		import datetime
	        now = datetime.datetime.now()
	        dzis_data = str(now)[:10]

		# ustalanie poczatkowej osoby, ktorej dotyczy wydatek (model osoba), jako obecnie zalogowana osoba (z tabeli auth_user)
		if user.pk == 1: # dla admina (z auth_user) brak domyślnej osoby docelowej (z modelu Osoba)
			domyslna_osoba = None 
		elif user.pk == 2: # dla bartka (z auth_user) domyślną osobą docelową jest 'Bartek' (z modelu Osoba)
			domyslna_osoba = 1
		elif user.pk == 3: # dla marii (z auth_user) domyślną osobą docelową jest 'Maria' (z modelu Osoba)
			domyslna_osoba = 3
                elif user.pk == 4: # dla mib (z auth_user) domyślną osobą docelową jest 'Dom' (z modelu Osoba)
                        domyslna_osoba = 2		
		else:
			domyslna_osoba = None

                # ustalanie poczatkowego zrodla, ktorego dotyczy wydatek
                if user.pk == 1: # dla admina (z auth_user) brak domyślnego zrodla finansowania (z modelu Zrodlo)
                        domyslne_zrodlo = None
                elif user.pk == 2: # dla bartka (z auth_user) domyślne zrodlo finansowania to 'Dobre Konto' (z modelu Zrodlo)
                        domyslne_zrodlo = 1
                elif user.pk == 3: # dla marii (z auth_user) domyślne zrodlo finansowania to 'Konto Maria' (z modelu Zrodlo)
                        domyslne_zrodlo = 2
                elif user.pk == 4: # dla mib (z auth_user) domyślne zrodlo finansowania to 'Konto Wspolne Biezace' (z modelu Zrodlo)
                        domyslne_zrodlo = 5		
                else:
                        domyslne_zrodlo = None

		# nowy, czysty formularz
		form = formularz_nowego_wpisu(initial={'zrodlo': 1, 'data' : dzis_data, 'kwota' : 1.00, 'osoba' : domyslna_osoba, 'zrodlo' : domyslne_zrodlo})
		flaga = "nie wyslano formularza!"

	# przygotowanie do wyświetlenia strony
        lista_par_miesiac_rok = daj_liste_par_miesiac_rok(user.pk)

	template = loader.get_template('panel_expenses_control/nowywydatek.html')
	slownik = {'form':form, 'flaga':flaga, 'lista_par_miesiac_rok' : lista_par_miesiac_rok}
        context = RequestContext(request, slownik)
        return HttpResponse(template.render(context))

def about(request):
        if not request.user.is_authenticated():
		powrotny_url = reverse('django.contrib.auth.views.login')
		return HttpResponseRedirect(powrotny_url)
        template = loader.get_template('panel_expenses_control/about.html')
        context = RequestContext(request, {})
        return HttpResponse(template.render(context))

def post(request):
        template = loader.get_template('panel_expenses_control/post.html')
        context = RequestContext(request, {})
        return HttpResponse(template.render(context))

def contact(request):
        template = loader.get_template('panel_expenses_control/contact.html')
        context = RequestContext(request, {})
        return HttpResponse(template.render(context))

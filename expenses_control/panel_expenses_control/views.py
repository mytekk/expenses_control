from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from .models  import *


def index(request):
	lista_kategorii = Kategoria.objects.all()
	template = loader.get_template('panel_expenses_control/index.html')
	context = RequestContext(request, {'lista_kategorii': lista_kategorii,})
	return HttpResponse(template.render(context))

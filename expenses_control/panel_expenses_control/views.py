from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from .models  import *
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect


def index(request):
	if not request.user.is_authenticated():
		powrotny_url = reverse('django.contrib.auth.views.login')
		return HttpResponseRedirect(powrotny_url)

	lista_kategorii = Kategoria.objects.all()
	template = loader.get_template('panel_expenses_control/index.html')
	context = RequestContext(request, {'lista_kategorii': lista_kategorii,})
	return HttpResponse(template.render(context))

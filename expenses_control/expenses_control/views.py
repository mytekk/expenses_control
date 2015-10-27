from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.contrib.auth import *
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect


def index(request):
        template = loader.get_template('expenses_control/index.html')
        context = RequestContext(request, {})
        return HttpResponse(template.render(context))
	  
def logout_page(request):
        logout(request)
        powrotny_url = reverse('expenses_control.views.index')
        return HttpResponseRedirect(powrotny_url)  

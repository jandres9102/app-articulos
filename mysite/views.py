from django.template.loader import get_template
from django.http import Http404,  HttpResponse
from django.template import Template, Context
import datetime
from django.shortcuts import render

def hello(request):
	return HttpResponse("Hola Mundo")

def current_datetime(request):
	now= datetime.datetime.now()
	return render(request, 'current_datetime.html', {'current_date': now})

def hours_ahead(request, offset):
	try:
		offset =int(offset)
	except ValueError:
		raise Http404()
	dt= datetime.datetime.now() + datetime.timedelta(hours=offset)
	return render(request,'hours_ahead.html',{'hour_offset':offset, 'next_time': dt})

from django.template.loader import get_template
from django.http import Http404,  HttpResponse
from django.template import Template, Context
import datetime
from django.shortcuts import render, render_to_response

def home(request):
	return render_to_response("home.html")
def article_list(request):
	return render_to_response("article_list.html")
def login(request):
	return render_to_response("login.html")
def modif_art(request):
	return render_to_response("modif_art.html")
def new_article(request):
	return render_to_response("new_article.html")
def register(request):
	return register("home.html")
def reset(request):
	return reset("home.html")

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

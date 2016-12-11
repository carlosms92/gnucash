from django.http import HttpResponse
from django.shortcuts import render_to_response
from apptfg.models import *

# Create your views here.

def home(request):
	return render_to_response('index.html')

def listaCuentas(request):
	cuentas=Accounts.objets.all()
	return render_to_response('index.html',{'cuentas':Accounts})

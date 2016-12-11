from django.http import HttpResponse
from django.shortcuts import render_to_response
from gnucash.models import *
from django.http import HttpResponseRedirect
import logging


# Create your views here.

def home(request):
	"""log = logging.getLogger(__name__)
	log.debug("prueba log")"""
	print("Hay que poner /cuentas en la URL para formulario que funciona")
	return render_to_response('index.html')

def listaCuentas(request):
	cuentas=Accounts.objects.all()
	return render_to_response('asiento_nuevo.html',{'cuentas': cuentas })

def guardar_asiento(request):
	print("llego aqui")
	if request.method=="POST":
		formulario = FormularioAsiento()
		#formulario = request.POST['fecha']
		transaction = Transaction()
		transaction.guid = int(str(uuid.uuid4()).replace('-',''),16)
		transaction.currency_guid = Commodities.objects.all().guid
		transaction.num = request.POST['num']
		#transaction.save()
		split = Splits()
		split.guid = int(str(uuid.uuid4()).replace('-',''),16)
		split.tx_guid = transaction.guid
		return render(request, 'asiento_nuevo_true.html', {'formulario': formulario})
		#return render_to_response('asiento_nuevo_true.html')

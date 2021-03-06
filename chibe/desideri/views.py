# -*- coding: utf-8 -*-
from django.http import HttpResponse, JsonResponse, HttpResponseNotFound, HttpResponseBadRequest
from django.views.generic import View
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from datetime import datetime
from django.shortcuts import render
from .models import Desiderio
from main.models import Gruppo, Utente

from django.db.models import Count
def desideri_new_home(request):
	now = datetime.now().date()

	desideri = []

	all_desideri = Desiderio.objects.filter(
		data_inizio__lte = now, 
		data_fine__gte = now,
		sku__gte=1
	).values(
		"id", 
		"nome",
		"descrizione_breve", 
		"in_evidenza", 
		"num_gruppo", 
		"immagine",
		"big_picture",
		"in_evidenza",
		"categoria__nome"
	)

	grouped = dict()

	for obj in all_desideri:
		grouped.setdefault(obj['categoria__nome'], []).append(obj)


	for g in grouped:
		items_des = grouped[g]

		json_d = {
			"categoria" : g,
			"desideri" : items_des
		}

		desideri.append(json_d)

	return JsonResponse(desideri, safe = False)

def desideri_home(request):
	now = datetime.now().date()

	all_desideri = Desiderio.objects.filter(
		data_inizio__lte = now, 
		data_fine__gte = now,
		sku__gte=1
	)

	desideri_premium = all_desideri.filter(in_evidenza = True).extra(select={'punti_piuma': "costo_riscatto/0.001"}).values(
		"id", 
		"nome",
		"descrizione_breve", 
		"in_evidenza", 
		"num_gruppo", 
		"punti_piuma",
		"immagine",
		"big_picture",
		"in_evidenza"
	)

	desideri_normali = all_desideri.filter(in_evidenza = False).extra(select={'punti_piuma': "costo_riscatto/0.001"}).values(
		"id", 
		"nome",
		"descrizione_breve", 
		"in_evidenza", 
		"num_gruppo", 
		"punti_piuma",
		"immagine",
		"big_picture",
		"in_evidenza"
	)

	desideri = list(desideri_premium) + list(desideri_normali)

	return JsonResponse(desideri, safe = False)

class desideri_id(View):
	@method_decorator(csrf_exempt)
	def dispatch(self, *args, **kwargs):
		return super(desideri_id, self).dispatch(*args, **kwargs)

	def get(self, request, id, *args, **kwargs):
		d = Desiderio.objects.get(pk = id)

		desiderio_json = {
			"id" : d.id,
			"nome" : d.nome,
			"descrizione_lunga" : d.descrizione_lunga,
			"immagine" : str(d.immagine),
			"num_gruppo" : d.num_gruppo,
			"punti_piuma" : d.punti_piuma()
		}

		return JsonResponse(desiderio_json, safe = False)

	def post(self, request, id, *args, **kwargs):
		user = request.user
		username = user.username

		utente = Utente.objects.get(username = username)		

		d = Desiderio.objects.get(pk = id)

		gruppo, created = Gruppo.objects.get_or_create(desiderio = d, utente_admin = utente)
		
		if created:
			gruppo.utenti.add(utente)

		utenti = gruppo.utenti.all().values("id")

		gruppo_json = {
			"id" : gruppo.id,
			"punti" : gruppo.punti,
			"punti_necessari" : gruppo.desiderio.punti_piuma(),
			"admin" : True,
			"utenti" : list(utenti),
			"nome" : gruppo.desiderio.nome,
			"num_gruppo" : gruppo.desiderio.num_gruppo
		}

		return JsonResponse(gruppo_json)


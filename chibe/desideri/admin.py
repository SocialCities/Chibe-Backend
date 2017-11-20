# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin

from .models import Desiderio, CategoriaDesiderio

@admin.register(CategoriaDesiderio)
class CategoriaDesiderioAdmin(admin.ModelAdmin):
	list_display = ['nome', 'id_immagine', 'descrizione']

@admin.register(Desiderio)
class DesiderioAdmin(admin.ModelAdmin):
	list_display = ['nome', 'descrizione_breve', 'punti_piuma', 'costo_riscatto', 'data_inizio', 'data_fine', 'num_gruppo', 'sku', 'in_evidenza']
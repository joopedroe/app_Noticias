from django.contrib import admin
from .models import *

@admin.register(Noticia)
class NoticiaAdmin(admin.ModelAdmin):
    pass

@admin.register(Pessoa)
class PessoaAdmin(admin.ModelAdmin)
from django.contrib import admin
from .models import *

@admin.register(Noticia)
class NoticiaAdmin(admin.ModelAdmin):
    pass

@admin.register(Pessoa)
class PessoaAdmin(admin.ModelAdmin):
    pass

@admin.register(Tag) 
class TagAdmin(admin.ModelAdmin):
    pass

@admin.register(MensagemDeContato)
class MensagemDeContatoAdmin(admin.ModelAdmin):
    readonly_fields=('data',)
from django.shortcuts import render
from django.views.generic import ListView, TemplateView

from .models import Noticia

class HomePageView(ListView):
    model=Noticia
    template_name='app_noticias/home.html'
    
class InicioView(TemplateView):
    template_name='app_noticias/inicial.html'
# Create your views here.

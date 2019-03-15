from django.shortcuts import render
from django.views.generic import ListView

from .models import Noticia

class HomePageView(ListView):
    model=Noticia
    template_name='app_noticias/home.html'
# Create your views here.

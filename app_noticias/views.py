from django.shortcuts import render
from django.views.generic import ListView, TemplateView
from django.http import HttpResponse, Http404

from .models import Noticia

class HomePageView(ListView):
    model=Noticia
    template_name='app_noticias/home.html'
    
class InicioView(TemplateView):
    template_name='app_noticias/inicial.html'

def DetalheNoticia(request, noticiaId):
    try:
        noticia=Noticia.objects.get(pk=noticiaId)
    except Noticia.DoesNoTExist:
        raise Http404('Noticia não encontrada')
    return render(request,"app_noticias/detalhe.html",{'noticia':noticia}) 

def EncontraTag(request, tag):
    noticia=Noticia.objects.filter(tags__nome__contains=tag)
    for i in noticia:
        print(i.titulo)
    return render(request,"app_noticias/inicial.html",{'noticia':noticia,'tag':tag})

def ContarNoticiaTemplate(request):
    total=Noticia.objects.count()
    return render(request,"app_noticias/resumo.html",{'total':total})

def ContarNoticia(request):
    total=Noticia.objects.count()
    html='''
    <html>
    <body>
    <h2> Resumo</h2>
    <p> A quantidade total de noticias é {}.</p>
    </boby>
    </html>'''.format(total)
    return HttpResponse(html)
# Create your views here.

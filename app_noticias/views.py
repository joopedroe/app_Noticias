from django.shortcuts import render, redirect
from django.views.generic import ListView, TemplateView, FormView
from django.http import HttpResponse, Http404
from django.urls import reverse
from .forms import *

from .models import Noticia

class HomePageView(ListView):
    model=Noticia
    template_name='app_noticias/noticiaHome.html'
    
'''class InicioView(TemplateView):
    template_name='app_noticias/inicial.html'''

def DetalheNoticia(request, noticiaId):
    try:
        noticia=Noticia.objects.get(pk=noticiaId)
    except Noticia.DoesNoTExist:
        raise Http404('Noticia não encontrada')
    return render(request,"app_noticias/noticiaDetalhe.html",{'noticia':noticia}) 

def EncontraTag(request, tag):
    noticia=Noticia.objects.filter(tags__nome__contains=tag)
    for i in noticia:
        print(i.titulo)
    return render(request,"app_noticias/noticiaTag.html",{'noticia':noticia,'tag':tag})

def ContarNoticiaTemplate(request):
    total=Noticia.objects.count()
    return render(request,"app_noticias/noticiaResumo.html",{'total':total})

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

class ContatoView(FormView):
    template_name='app_noticias/contato.html'
    form_class=ContatoForm
    
    def form_valid(self, form):
        dados=form.clean()
        mensagem=MensagemDeContato(nome=dados['nome'],email=dados['email'],mensagem=dados['mensagem'])
        mensagem.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('contato_sucesso')

class ContatoSucessoView(TemplateView):
    template_name='app_noticias/contato_sucesso.html'

class CadastroNoticiaView(FormView):
    template_name='app_noticias/cadastroNoticia.html'
    form_class=CadastroNoticiaForm

    def form_valid(self, form):
        dados=form.clean()
        noticia=Noticia(titulo=dados['titulo'],conteudo=dados['conteudo'])
        noticia.save()
        return super().form_valid(form)

def get_cadastroNoticia(request):
    if request.method == "POST":
        form=CadastroNoticia2Form(request.POST)
        if form.is_valid():  
            form.save()
            return redirect('home')
    else:
        print('aaaaaaaaaaaaaaaaaa')
        form=CadastroNoticia2Form()
    return render (request,'app_noticias/cadastroNoticia2.html',{'form':form})
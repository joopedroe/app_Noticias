from django.urls import path
from . import views
from app_noticias.views import *

urlpatterns=[
    path('',views.HomePageView.as_view(), name='home'),
    path('resumo/',ContarNoticiaTemplate),
    path('<int:noticiaId>/',DetalheNoticia,name='detalhe'),
    path('<str:tag>/',EncontraTag,name='encontratag'),
    path('contato/chat/',views.ContatoView.as_view(), name='contato'),
    path('contato_sucesso',views.ContatoSucessoView.as_view(),name='contato_sucesso'),

]

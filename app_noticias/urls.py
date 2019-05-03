from django.urls import path
from . import views
from app_noticias.views import *

urlpatterns=[
    path('',views.HomePageView.as_view(), name='home'),
    path('noticia/resumo/',ContarNoticiaTemplate),
    path('noticia/<int:noticiaId>/',DetalheNoticia,name='detalhe'),
    path('noticia/resumo/<str:tag>/',EncontraTag,name='encontratag'),

]

from django.urls import path
from . import views
from app_noticias.views import *

urlpatterns=[
    path('',views.HomePageView.as_view(), name='home'),
    path('inicio/',InicioView.as_view()),

]

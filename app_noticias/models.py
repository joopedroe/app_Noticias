from django.db import models

class Noticia(models.Model):
    class Meta:
        verbose_name = 'Notícia'
        verbose_name_plural= 'Notícias'

    titulo=models.CharField('título', max_length=128)
    conteudo= models.TextField()
    data_criacao=models.DateTimeField()
    data_publicacao=models.DateTimeField()
    publicado=models.BooleanField()

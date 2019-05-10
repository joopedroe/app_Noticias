from django.db import models
from django.contrib.auth.models import User


class Pessoa(models.Model):
    usuario= models.OneToOneField(User, on_delete=models.CASCADE,
        verbose_name='Usuario')
    nome=models.CharField('Nome',max_length=128)
    data_de_nascimento=models.DateTimeField('data de nascimento',blank=True,null=True)
    telefone_celular=models.CharField("Telefone Celular", max_length=15, help_text='Numero de telefone celular no formato (99)99999-9999', null=True, blank=True)
    telefone_fixo=models.CharField("Telefone Fixo", max_length=15, help_text='Numero de telefone Fixo no formato (99)99999-9999', null=True, blank=True)
    email=models.EmailField('E-mail',null=True, blank=True)

    def __str__ (self):
        return self.nome


class Tag(models.Model):
    nome= models.CharField(max_length=64)
    slug= models.CharField(max_length=64)

    def __str__(self):
        return (self.nome)


class Noticia(models.Model):
    class Meta:
        verbose_name = 'Notícia'
        verbose_name_plural= 'Notícias'
        
    tags= models.ManyToManyField(Tag,blank=True,null=True)
    autor= models.ForeignKey(Pessoa, on_delete=models.CASCADE,blank=True,null=True)
    titulo=models.CharField('título', max_length=128)
    conteudo= models.TextField()
    data_criacao=models.DateTimeField(blank=True,null=True)
    data_publicacao=models.DateTimeField(blank=True,null=True)
    publicado=models.BooleanField(blank=True,null=True)

class MensagemDeContato(models.Model):
    class Meta:
        verbose_name='Mensagem de contato'
        verbose_name_plural='Mensagens de Contato'
    
    nome=models.CharField(max_length=128)
    email=models.EmailField('E-mail', null=True,blank=True)
    mensagem=models.TextField()
    data=models.DateTimeField(auto_now_add=True)
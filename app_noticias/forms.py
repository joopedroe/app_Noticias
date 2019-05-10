from django import forms
from django.forms import ModelForm, models
from .models import MensagemDeContato, Noticia, User

class ContatoForm(forms.Form):
    nome=forms.CharField(max_length=128,min_length=12)
    email=forms.EmailField(required=False)
    mensagem=forms.CharField(widget=forms.Textarea)


    def clean(self):
        dados=super().clean()
        email=dados.get('email',None)
        mensagem=dados.get('mensagem')
        if '@gmail.com' in email:
            self.add_error('email','Provedor de e-mail não suportado  @gmail.com')

        palavras=['problema','defeito','erro']
        for palavra in palavras:
            if palavra in mensagem.lower():
                self.add_error('mensagem','Mensagem contem palavras não permitidas')
        return dados

class CadastroNoticiaForm(forms.Form):
    titulo=forms.CharField(max_length=128)
    conteudo=forms.CharField(widget=forms.Textarea)

    def clean(self):
        dados=super().clean()
        titulo=dados.get('titulo')
        conteudo=dados.get('conteudo')
        return dados

class CadastroNoticia2Form(ModelForm):

    class Meta:
        model = Noticia
        fields =['titulo','conteudo','autor','tags']

class PaginaLogin(ModelForm):
    
    class Meta:
        model=User
        fields=['username','password']
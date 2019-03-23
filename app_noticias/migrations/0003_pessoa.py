# Generated by Django 2.1.7 on 2019-03-23 00:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app_noticias', '0002_auto_20190322_1923'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=128, verbose_name='Nome')),
                ('data_de_nascimento', models.DateTimeField(blank=True, null=True, verbose_name='data de nascimento')),
                ('telefone_celular', models.CharField(blank=True, help_text='Numero de telefone celular no formato (99)99999-9999', max_length=15, null=True, verbose_name='Telefone Celular')),
                ('telefone_fixo', models.CharField(blank=True, help_text='Numero de telefone Fixo no formato (99)99999-9999', max_length=15, null=True, verbose_name='Telefone Fixo')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='E-mail')),
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuario')),
            ],
        ),
    ]
# Generated by Django 2.1.7 on 2019-03-22 22:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_noticias', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='noticia',
            name='data_criacao',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='noticia',
            name='data_publicacao',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='noticia',
            name='publicado',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]

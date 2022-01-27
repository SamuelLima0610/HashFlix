from django.db import models
from django.utils import timezone

LISTA_CATEGORIA = (
    ("ANALISES", "Análises"),
    ("PROGRAMACAO", "Programação"),
    ("APRESENTACAO", "Apresentação"),
    ("OUTROS","Outros")
)


# Create your models here.
class Filme(models.Model):
    titulo = models.CharField(max_length=100)
    thumb = models.ImageField(upload_to="thumb_filmes")
    descricao = models.TextField(max_length=1000)
    categoria = models.CharField(max_length=15, choices=LISTA_CATEGORIA)
    visualizacoes = models.IntegerField(default=0)
    data_criacao = models.DateTimeField(default=timezone.now)
from django.shortcuts import render
from .models import Filme
from django.views.generic import TemplateView, ListView, DetailView


class HomePage(TemplateView):
    template_name = "homepage.html"


class HomeFilmes(ListView):
    template_name = "homefilmes.html"
    model = Filme


class DetalhesFilme(DetailView):
    template_name = "detalhesfilme.html"
    model = Filme

    def get(self, request, *args, **kwargs):
        filme = self.get_object()
        filme.visualizacoes += 1
        filme.save()
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(DetalhesFilme, self).get_context_data(**kwargs)
        filmes_relacionados = Filme.objects.filter(categoria=self.get_object().categoria)
        context['filmes_relacionados'] = filmes_relacionados
        return context



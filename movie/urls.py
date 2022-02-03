from django.urls import path, include
from .views import HomePage, HomeFilmes


urlpatterns = [
    path('', HomePage.as_view()),
    path('filmes/',HomeFilmes.as_view())
]
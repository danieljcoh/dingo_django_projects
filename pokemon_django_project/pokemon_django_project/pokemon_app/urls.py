from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="home"),
    path("<str:pokemon_id>", views.pokemon_details, name="pokemon_details")
]

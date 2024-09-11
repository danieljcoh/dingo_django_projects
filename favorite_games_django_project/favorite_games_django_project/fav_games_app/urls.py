from django.urls import path
from . import views


urlpatterns = [
    path("", views.index),
    path("<str:game>", views.game_details, name="specific_game")
]

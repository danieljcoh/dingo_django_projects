from django.urls import path
from . import views


urlpatterns = [
    path("", views.index),
    path("<str:game>", views.specific_game_details)
]

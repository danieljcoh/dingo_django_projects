from django.urls import path
from . import views


urlpatterns = [
    path("", views.index),
    path("<game>", views.specific_game_details)
]

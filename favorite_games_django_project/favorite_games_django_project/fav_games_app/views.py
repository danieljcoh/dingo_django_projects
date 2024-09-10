from django.shortcuts import render
from django.http import Http404, HttpResponse

# Create your views here.

list_of_fav_games = {
    "jak_and_daxter": {
        "title": "Jak and Daxter",
        "developer": "Naughty Dog"
    },
    "bioshock": {
        "title": "Bioshock 1",
        "developer": "2K"
    },
    "rachet_and_clank": {
        "title": "Rachet and Clank",
        "developer": "Insomniac Games"
    }
}


def index(request):
    return render(request, "fav_games_app/index.html", {
        "games": list_of_fav_games
    })


def specific_game_details(request, game):
    if game in list_of_fav_games:
        return render(request, "fav_games_app/game.html", {
            "game": game.title
        })
    else:
        return HttpResponse("This Game is Not Supported")

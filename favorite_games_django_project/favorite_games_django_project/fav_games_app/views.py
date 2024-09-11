from django.urls import reverse
from django.shortcuts import render, reverse
from django.http import Http404, HttpResponse, HttpResponseRedirect, HttpResponseNotFound

# TODO: add a "why" section to the list of fav games object
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
    },
    "helldivers": {
        "title": "Helldivers 2",
        "developer": "Arrowhead"
    },
    "ghost_tsushima": {
        "title": "Ghost of Tsushima",
        "developer": None
    }
}


def index(request):
    game_links = []
    for game in list_of_fav_games.keys():
        # Reverse to generate URL
        game_url = reverse('specific_game', args=[game])
        game_links.append(
            {"title": list_of_fav_games[game]["title"],
             "developer": list_of_fav_games[game]["developer"],
             "url": game_url})

    return render(request, "fav_games_app/index.html", {
        "game_links": game_links
    })


def game_details(request, game):
    list_of_games = list(list_of_fav_games.keys())

    if game in list_of_games:
        return render(request, "fav_games_app/game.html", {
            "game_title": list_of_fav_games[game]["title"],
            "game_developer": list_of_fav_games[game]["developer"],
        })
    else:
        return HttpResponseNotFound(f"<h1>The Game {game} is Not Supported</h1>")

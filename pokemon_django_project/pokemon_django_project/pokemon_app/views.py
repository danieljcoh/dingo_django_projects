from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.
pokemon_list = {
    1: {
        "name": "Bulbasaur",
        "type": ["grass", "poison"],
        "description": "Bulbasaur is a small, quadruped Pokémon with a large plant bulb on its back."
    },
    2: {
        "name": "Ivysaur",
        "type": ["grass", "poison"],
        "description": "Ivysaur is a bigger and stronger evolution of Bulbasaur."
    },
    3: {
        "name": "Venusaur",
        "type": ["grass", "poison"],
        "description": "Venusaur is the fully evolved form of Bulbasaur, with a large flower blooming on its back."
    },
    4: {
        "name": "Charmander",
        "type": ["fire"],
        "description": "Charmander is a fire-type Pokémon that has a small flame burning at the tip of its tail."
    },
    5: {
        "name": "Charmeleon",
        "type": ["fire"],
        "description": "Charmeleon is the evolved form of Charmander, with a fiercer flame on its tail."
    },
    6: {
        "name": "Charizard",
        "type": ["fire", "flying"],
        "description": "Charizard is a large, dragon-like Pokémon that can fly and breathe intense flames."
    },
    7: {
        "name": "Squirtle",
        "type": ["water"],
        "description": "Squirtle is a small turtle Pokémon known for withdrawing into its shell to defend itself."
    },
    8: {
        "name": "Wartortle",
        "type": ["water"],
        "description": "Wartortle is the evolved form of Squirtle, with larger ears and a bushy tail."
    },
    9: {
        "name": "Blastoise",
        "type": ["water"],
        "description": "Blastoise is a large tortoise Pokémon with water cannons mounted on its shell."
    },
    10: {
        "name": "Caterpie",
        "type": ["bug"],
        "description": "Caterpie is a small, worm-like Pokémon known for its bright green color and voracious appetite."
    }
}


def index(request):
    return render(request, "pokemon_app/index.html", {
        "pokemon_list": pokemon_list
    })


def pokemon_details(request, pokemon_id):
    try:
        specific_pokemon_id = int(pokemon_id)
        specific_pokemon_name = pokemon_list[specific_pokemon_id]["name"]
        specific_pokemon_type = pokemon_list[specific_pokemon_id]["type"]
        specific_pokemon_description = pokemon_list[specific_pokemon_id]["description"]
    except:
        return HttpResponseNotFound("<h1>Pokemon not found!</h1>")

    return render(request, "pokemon_app/pokemon_details.html", {
        "pokemon_name": specific_pokemon_name,
        "pokemon_type": specific_pokemon_type,
        "pokemon_description": specific_pokemon_description
    })

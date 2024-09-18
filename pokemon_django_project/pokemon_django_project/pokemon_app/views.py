from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.
pokemon_list = {
    1: {
        "name": "Primeape",
        "type": ["Fighting"],
        "stats": {
            "hp": 65,
            "attack": 105,
            "defense": 60,
            "special_attack": 60,
            "special_defense": 70,
            "speed": 95
        },
        "description": "Primeape is a fast physical attacker with high Attack and Speed but frail defenses.",
        "img_location": "pokemon_app/images/primeape_img.jpg"
    },
    2: {
        "name": "Electabuzz",
        "type": ["Electric"],
        "stats": {
            "hp": 65,
            "attack": 83,
            "defense": 57,
            "special_attack": 95,
            "special_defense": 85,
            "speed": 105
        },
        "description": "Electabuzz is a fast special attacker, known for its high Speed and decent Special Attack.",
        "img_location": "pokemon_app/images/electabuzz_img.jpg"
    },
    3: {
        "name": "Lapras",
        "type": ["Water", "Ice"],
        "stats": {
            "hp": 130,
            "attack": 85,
            "defense": 80,
            "special_attack": 85,
            "special_defense": 95,
            "speed": 60
        },
        "description": "Lapras is a bulky Water/Ice type with high HP and strong defenses, making it a great tank.",
        "img_location": "pokemon_app/images/lapras_img.jpg"
    },
    4: {
        "name": "Gengar",
        "type": ["Ghost", "Poison"],
        "stats": {
            "hp": 60,
            "attack": 65,
            "defense": 60,
            "special_attack": 130,
            "special_defense": 75,
            "speed": 110
        },
        "description": "Gengar is a speedy special attacker with high Special Attack and Speed, but low defenses.",
        "img_location": "pokemon_app/images/gengar_img.jpg"
    },
    5: {
        "name": "Umbreon",
        "type": ["Dark"],
        "stats": {
            "hp": 95,
            "attack": 65,
            "defense": 110,
            "special_attack": 60,
            "special_defense": 130,
            "speed": 65
        },
        "description": "Umbreon is a defensive Pokémon, excelling in Special Defense and Defense, making it a great tank.",
        "img_location": "pokemon_app/images/umbreon_img.jpg"
    },
    6: {
        "name": "Dragonite",
        "type": ["Dragon", "Flying"],
        "stats": {
            "hp": 91,
            "attack": 134,
            "defense": 95,
            "special_attack": 100,
            "special_defense": 100,
            "speed": 80
        },
        "description": "Dragonite is a versatile physical and special attacker with great bulk and high Attack.",
        "img_location": "pokemon_app/images/dragonite_img.jpg"
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
        # specific_pokemon_image = pokemon_list[specific_pokemon_id]["image_location"]
    except:
        return HttpResponseNotFound("<h1>Pokemon not found!</h1>")

    return render(request, "pokemon_app/pokemon_details.html", {
        "pokemon_name": specific_pokemon_name,
        "pokemon_type": specific_pokemon_type,
        "pokemon_description": specific_pokemon_description,
        # "pokemon_image": specific_pokemon_image
    })

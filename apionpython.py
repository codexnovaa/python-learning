#Connecting api using python

import requests

baseUrl = "https://pokeapi.co/api/v2/"

def getPokemonInfo(name):
    url = f"{baseUrl}/pokemon/{name}"
    responese = requests.get(url)
    
    if responese.status_code == 200:
        pokemonData = responese.json()
        return pokemonData
    else:
        print(f"Failed to retrieve data {responese.status_code}")
    
if __name__ == "__main__":
    pokemonName = input("Enter pokemon name: ").lower()
    pokemonInfo = getPokemonInfo(pokemonName)
    
    if pokemonInfo:
        print(f"Name: {pokemonInfo["name"].capitalize()}")
        print(f"ID: {pokemonInfo["id"]}")
        print(f"Height: {pokemonInfo["height"]}")
        print(f"Weight: {pokemonInfo["weight"]}")
        print(f"100 - {pokemonInfo["stats"][0]["stat"]["name"]}")



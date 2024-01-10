import requests

response = requests.get('https://pokeapi.co/api/v2/pokemon/pikachu')

# The response from the API is a JSON object, so you can convert it to a Python dictionary using .json()
data = response.json()

def print_pokemon_moves(pokemon_name):
    response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{pokemon_name}')
    data = response.json()

    for move in data['moves']:
        print(move['move']['name'])

# Use the function to print all moves for Ditto
# print_pokemon_moves('pikachu')


# # Get the data for a move
# response = requests.get('https://pokeapi.co/api/v2/move/mega-punch')
# data = response.json()

# # The move's description is in the 'flavor_text_entries' list
# # Each item in the list is a dictionary with information about the move in a specific language and version of the game
# # Here we're getting the description in English from the first item in the list
# description = data['flavor_text_entries'][0]['flavor_text']

# print(description)


import requests

class Pokemon:
    def __init__(self, name):
        response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{name}')
        data = response.json()

        self.name = name
        self.health = 100  # This is a placeholder value, replace with actual health if available
        self.pokedex_number = data['id']
        self.moves = [move['move']['name'] for move in data['moves'][:4]]
        self.level = 5

    def print_info(self):
        print(f"Name: {self.name}")
        print(f"Health: {self.health}")
        print(f"Pokedex Number: {self.pokedex_number}")
        print(f"Moves: {self.moves}")
        print(f"Level: {self.level}")


# Create a Pokemon object for Pikachu
snorlax = Pokemon('snorlax')

# Print Pikachu's info
snorlax.print_info()

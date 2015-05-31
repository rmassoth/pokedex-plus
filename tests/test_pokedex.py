import pokedex

char = pokedex.Pokemon('Charmander', 'Fire')
bulb = pokedex.Pokemon('Bulbasaur', 'Grass')
squirt = pokedex.Pokemon('Squirtle', 'Water')
my_pokemon = [char, bulb]

def test_get_best_pokemon():
	assert(pokemon.get_best_pokemon(char, bulb), 2)

def test_get_best_pokemon():
	assert(pokemon.get_best_pokemon(bulb, char), 0.5)
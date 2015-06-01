from pokedex import pokedex

char = pokedex.Pokemon('Charmander', 'Fire')
bulb = pokedex.Pokemon('Bulbasaur', 'Grass')
squirt = pokedex.Pokemon('Squirtle', 'Water')
my_pokemon = [char, bulb]

def test_get_best_pokemon_mine_is_stronger():
	assert pokedex.get_best_pokemon(char, bulb) == char

def test_get_best_pokemon_mine_is_weaker():
	assert pokedex.get_best_pokemon(char, squirt) == squirt

def test_get_effectiveness_mine_is_stronger():
	assert pokedex.get_effectiveness(char, bulb) == 2

def test_get_effectiveness_theirs_is_stronger():
	assert pokedex.get_effectiveness(bulb, char) == 0.5

def test_get_effectiveness_equal():
	assert pokedex.get_effectiveness(char, char) == 1
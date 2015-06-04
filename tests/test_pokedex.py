from pokedex import pokedex

char = pokedex.get_pokemon('charmander')
bulb = pokedex.get_pokemon('bulbasaur')
squirt = pokedex.get_pokemon('squirtle')
pikachu = pokedex.get_pokemon('pikachu')
snover = pokedex.get_pokemon('snover')
my_pokemon = [char, bulb, squirt, pikachu]

def test_get_best_pokemon_mine_is_stronger():
	assert pokedex.get_best_pokemon(char, bulb) == char

def test_get_best_pokemon_mine_is_weaker():
	assert pokedex.get_best_pokemon(char, squirt) == squirt

def test_get_effectiveness_mine_is_stronger():
	assert pokedex.get_effectiveness(char, bulb) == 2

def test_get_effectiveness_theirs_is_stronger():
	assert pokedex.get_effectiveness(bulb, char) == 0.5

def test_get_effectiveness_equal():
	assert pokedex.get_effectiveness(char, pikachu) == 1

def test_get_pokemon():
	my_pokemon = pokedex.get_pokemon('charmander')
	assert my_pokemon.name_ == 'charmander'

def test_effectiveness_dual_type():
	assert pokedex.get_effectiveness(char, snover) == 4
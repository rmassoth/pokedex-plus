import json, os
"""
This is the main program that contains the Pokemon class, functions for creating instances by name, loading the database file and 
getting the multiplier for a combination of pokemon types.

TODO:
Currently, the function only compares the types of pokemon and returns the weaknesses to the type.  This is a simple multiplier 
and it stacks if there are dual types.  

1. I want to create another layer to the database which includes moves and their types as 
	well as what levels they can acheive these moves.  This will aide in better selecting the types of pokemon because the defensive type
	is only really effective against the attack type. Attack types can be learned by pokemon with defense types that don't match.  This 
	program assumes for now that a pokemon of 'X' type will likely have attacks of 'X' type as well and therefore is a worst (or best) case scenario.

2. I would like to add partial string searching with suggestions.  There are a lot of pokemon, only a hard-core gamer would know them all.
"""

class Pokemon:
	"""
	This class may be moved eventually but for now it can be here because the program is small
	"""
	def __init__(self, name_, type_ = ['normal',], level_ = 1):
		self.name_ = name_
		self.type_ = type_
		self.level_ = level_

	def __str__(self):
		return str(self.__dict__)

	def __eq__(self, other):
		return self.__dict__ == other.__dict__

#dict of all pokemon. Read in from a file with a JSON string in it.  Got the info from pokemondb.net, the Pokemon database.  Thanks to them!
all_pokemon = {}
pokedb_path = os.path.dirname(__file__)

def get_best_pokemon(my_pokemon, their_pokemon):
	if(get_effectiveness(my_pokemon, their_pokemon) >= 1):
		return my_pokemon
	else:
		return their_pokemon

def best_first_list(my_pokemon, their_pokemon):
	for pokemon in my_pokemon:
		get_effectiveness(pokemon, their_pokemon)

def load_pokemon_from_file():
	"""
	Load 'database' of types.  I considered using an actual database, such as sqlite, but the data never changes
	so that would be overkill at this point.
	"""
	try:
		pokedb = open(pokedb_path + '/pokedb')
		all_pokemon = json.loads(pokedb.readline())
		return all_pokemon
	except FileNotFoundError:
		print('Pokedb file not found')
	else:
		pokedb.close()

all_pokemon = load_pokemon_from_file()

def get_pokemon(name):
	"""
	Find pokemon by name from dictionary and return Pokemon object with name and list of types.
	"""
	try:
		pokemon_type = all_pokemon[name]
		my_pokemon = Pokemon(name, pokemon_type)
		return my_pokemon
	except KeyError:
		print('Cannot find pokemon with name "' + name + '"')


def get_effectiveness(attacker, defender):
	"""
	Loop through attacker types and multiply by defender types.  Multiples stack.
	"""
	try:
		effectiveness = 1
		for attack_type in attacker.type_:
			for defense_type in defender.type_:
				if defense_type in decision_table[attack_type]:
					effectiveness = effectiveness * decision_table[attack_type][defense_type]
				else:
					# if types have no special effectiveness, then multiplier is 1 and thus no change
					pass
		return effectiveness
	except KeyError:
		return 1

decision_table = {
"""
This is a simple decision table 2D dictionary with 'attack' type for 1st keys and 'defense' types for 2nd keys with values
being the multipliers for those combinations.  If a key combination doesn't exist, we assume 'normal' effectiveness (no multiple).  
"""
	'normal': {
		'rock': 0.5,
		'ghost': 0,
	},
	'fire': {
		'fire': 0.5,
		'water': 0.5,
		'grass': 2,
		'ice': 2,
		'bug': 2,
		'rock': 0.5,
		'dragon': 0.5,
	},
	'water': {
		'fire': 2,
		'water': 0.5,
		'grass': 0.5,
		'ground': 2,
		'rock': 2,
		'dragon': 0.5,
	},
	'electric': {
		'water': 2,
		'electric': 0.5,
		'grass': 0.5,
		'ground': 0,
		'flying': 2,
		'dragon': 0.5,
	},
	'grass': {
		'fire': 0.5,
		'water': 2,
		'grass': 0.5,
		'poison': 0.5,
		'ground': 2,
		'flying': 0.5,
		'bug': 0.5,
		'rock': 2,
		'dragon': 0.5,
	},
	'ice':{
		'water': 0.5,
		'grass': 2,
		'ice': 0.5,
		'ground': 2,
		'flying': 2,
		'dragon': 2,
		},
	'fighting':{
		'normal': 2,
		'ice': 2,
		'poison': 0.5,
		'flying': 0.5,
		'psychic': 0.5,
		'bug': 0.5,
		'rock': 2,
		'ghost': 0,
	},
	'poison':{
		'grass': 2,
		'poison': 0.5,
		'ground': 0.5,
		'bug': 2,
		'rock': 0.5,
		'ghost': 0.5,
	},
	'ground':{
		'fire': 2,
		'electric': 2,
		'grass': 0.5,
		'poison': 2,
		'flying': 0,
		'bug': 0.5,
		'rock': 2,
	},
	'flying':{
		'electric': 0.5,
		'grass': 2,
		'fighting': 2,
		'bug': 2,
		'rock': 0.5,
		},
	'psychic':{
		'fighting': 2,
		'poison': 2,
		'psychic': 0.5,
	},
	'bug':{
		'fire': 0.5,
		'grass': 2,
		'fighting': 0.5,
		'poison': 2,
		'flying': 0.5,
		'psychic': 2,
	},
	'rock':{
		'fire': 2,
		'ice': 2,
		'fighting': 0.5,
		'ground': 0.5,
		'flying': 2,
		'bug': 2,
	},
	'ghost':{
		'normal': 0,
		'psychic': 0,
		'ghost': 2,
	},
	'dragon':{
		'dragon': 2,
	},					  		

				  }
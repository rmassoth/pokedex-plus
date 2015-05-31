#imports

def get_best_pokemon(my_pokemon, their_pokemon):
	best_pokemon = ''
	return best_pokemon

def best_first_list(my_pokemon, their_pokemon):
	pass

def compare_two_pokemon_by_type(poke1, poke2):
	decision_table = {
					  'Fire':{
					  		  'Water':0.5,
					  		  'Grass':2,
					  		  'Fire':1,
					  		  },
					  'Water':{
					  		  'Fire':2,
					  		  'Grass':0.5,
					  		  'Water':1,
					  		  },
					  'Grass':{
					  		  'Fire':0.5,
					  		  'Water':2,
					  		  'Grass':1,
					  		  }
					  }

	effectivness = decision_table[poke1.type_][poke2.type_]
	return effectivness
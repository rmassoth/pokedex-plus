import sqlite3

cnx = sqlite3.connect("./pokedex/pokemon.db")
cursor = cnx.cursor()
create_table = "CREATE TABLE IF NOT EXISTS pokemon(id INT PRIMARY KEY, name TEXT, type TEXT);"
try:
	cnx.execute(create_table)
except:
	print("Some error occured")


def add_pokemon(pokemon):
	sql = "INSERT INTO pokemon(`name`, `type`) VALUES('{}', '{}');".format(pokemon.name_, pokemon.type_)
	try:
		error = cursor.execute(sql)
		cnx.commit()
	except:
		print("Error inserting new pokemon")
		print(pokemon.name_, pokemon.type_)

def get_pokemon():
	sql = "select * from pokemon"
	try:
		cursor.execute(sql)
		data = cursor.fetchall()
		return data
	except:
		print("Something went horribly wrong")
# by jon hudgins and jackie faselt 

# reads superheroes.json (in this folder)
import csv
import json

# read superheros.json
with open('superheroes.json', 'r') as f:
	superheroes = json.load(f)

# write a header to the csv file 

	
# print(superheroes)

with open('testwrite.csv', 'w') as f:
	writer = csv.writer(f)
	header = ["name", "age", "secretIdentity", "powers", "squadName", "homeTown", "formed", "secretBase", "active"]
	writer.writerow(header)
  

# creates an empty array called powers 
	powers = []

	# Loop through the members of the squad and 
	members = superheroes['members']
	squadName = superheroes ['squadName']
	homeTown = superheroes ['homeTown']
	formed = superheroes ['formed']
	secretBase = superheroes ['secretBase']
	active = superheroes ['active']
	for member in members:

		name = member['name']

		this_members_powers = member['powers']

		age = member['age']
		secretIdentity = member['secretIdentity']
		row = [name, age, secretIdentity, this_members_powers, squadName,homeTown,formed,secretBase,active]



		#with open('testwrite.csv', 'w') as f:
		writer.writerow(row)


# append the powers of each to the powers array 



# prints those powers to the terminal 

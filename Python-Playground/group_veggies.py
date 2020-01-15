# jackie and Jonathon
import csv
import json
from pprint import pprint

# read vegtablescsv

with open('vegetables.csv', 'r') as f:
	reader = csv.DictReader(f)
	rows = list(reader)
	rows = [dict(row) for row in rows]

	vegetables = rows 

# group veggies by color 
vegtables_by_color = {}

for veggie in vegetables:
	color = veggie['color']
	if color in vegtables_by_color:
		vegtables_by_color[color].append(veggie)
	else:
		vegtables_by_color[color] = [veggie]

pprint(vegtables_by_color)

# output into json 

with open('group_veg.json', 'w') as f:
    json.dump(vegtables_by_color, f, indent=2)
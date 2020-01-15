# by jonathan hudgins and jackie faselt
import csv


vegetables = [
 {"name": "eggplant", "color": "purple"},
 {"name": "tomato", "color": "red"},
 {"name": "corn", "color": "yellow"},
 {"name": "okra", "color": "green"},
 {"name": "arugula", "color": "green"},
 {"name": "broccoli", "color": "green"},
]


# 1. Loops through each vegetable


with open('vegetables.csv', 'w') as f:
	writer = csv.writer(f)
	writer.writerow(['name', 'color'])

	for veggie in vegetables:
		writer.writerow([veggie["name"], veggie["color"]])




# 2. In the loop, write the name of each vegetable and the color into a CSV called vegetables.csv
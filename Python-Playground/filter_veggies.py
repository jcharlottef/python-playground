# Jackie and Johnathon 



#import pandas as pd

#read vegtables
#vegtables = pd.read_csv ("vegtables.csv")

import csv
import json

#read in csv

with open('vegetables.csv', 'r') as f:
	reader = csv.DictReader(f)
	rows = list(reader)
	rows = [dict(row) for row in rows]

	vegetables = rows 

#create whitelist
whitelist = ['okra', 'arugula','broccoli']

#loop
green_veg = []

for veggie in vegetables: 
	if veggie['name'] in whitelist:
		green_veg.append(veggie)


print(green_veg)

#save to json

with open('green_veg.json', 'w') as f:
    json.dump(green_veg, f, indent=2)






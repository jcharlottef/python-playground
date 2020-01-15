# jonathan hudgins and jackie faselt 

# 1. Read vegetables.csv (see previous section) 
# into a variable called vegetables.
import csv
import json


with open('vegetables.csv', 'r') as f:
    reader = csv.DictReader(f)
    vegetables = list(reader)
    vegetables = [dict(veggie) for veggie in vegetables] 


# Convert OrderedDict to regular dict

with open('vegetables.json', 'w') as f:
    json.dump(vegetables, f, indent =4) 


# print the variable vegetables 



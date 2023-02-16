import json

data = {}
with open("./example.json", 'r') as file:
    data = json.load(file)

for i in data["movies"]:
    if i['year'] > 2000:
        print(i['title'])
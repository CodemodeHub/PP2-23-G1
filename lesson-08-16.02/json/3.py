import json

new_actor = {
  "name": "Tom Holland",
  "age": 17,
  "nationality": "American",
  "occupation": "Actor",
  "movies": [
      {
        "title": "Spider Man",
        "year": 2021,
        "role": "Peter Parker"
      },
  ]
}

with open("./example.json", 'w') as file:
    json.dump(new_actor, file)
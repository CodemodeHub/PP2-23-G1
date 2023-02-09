import json

# JSON string
json_string = '''
    {
        "name": "Alikhan",
        "age": 19,
        "city": "Almaty",
        "courses": ["Web", "iOS", "Sociology", "Kazakh", "ITN", "IBM"]
    }
'''

data = '''
    "gjfdsogbdsj": {
        id: "1",
        name: "B"
    },
    "fsdjkfsd": {
        id: "2",
        name: "A"
    }
'''

# parse the JSON string
parsed_json = json.loads(json_string)

# access the elements
name = parsed_json["name"]
age = parsed_json["age"]
city = parsed_json["city"]
courses = parsed_json["courses"]

print(name)
print(age)
print(city) 
print(courses)
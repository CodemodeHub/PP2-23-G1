import json

# A sample Python object
person = {
    "firstName": "John",
    "lastName": "Doe",
    "age": 30,
    "address": {
        "streetAddress": "21 2nd Street",
        "city": "New York",
        "state": "NY",
        "postalCode": "10021"
    },
    "phoneNumbers": [
        {
            "type": "home",
            "number": "212 555-1234"
        },
        {
            "type": "office",
            "number": "646 555-4567"
        }
    ]
}

# Encoding the Python object into JSON
person_json = json.dumps(person, indent=4)

# print(person)
print(person_json)
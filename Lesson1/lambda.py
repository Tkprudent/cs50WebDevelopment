people = [
    {"name": "Harry", "house": "Gryfindor"},
    {"name": "James", "house": "Ravenclaw"},
    {"name": "Cho", "house": "Denmark"},
    {"name": "Habrel", "house": "Greeceland"},
    {"name": "Kaxy", "house": "Nigeria"},
]

#def f(person):
#    return person["house"]

#person is the input and person["name"] is output
people.sort(key = lambda person: person["name"])

print(people)
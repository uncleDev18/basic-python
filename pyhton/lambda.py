people = [
    {"name": "Brian", "house": "Calapan"},
    {"name": "Maureen", "house": "Barcenaga"},
    {"name": "Remar", "house": "Masaguing"},
    {"name": "Ivan", "house": "Mandaluyong"}
]

people.sort(key=lambda person: person["house"])

print(people)
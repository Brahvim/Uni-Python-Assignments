import json

students = {
    "Ansh": 50,
    "Brahvim": 5,
}

f = open("students.json", "w")
json.dump(students, f)
f.close()

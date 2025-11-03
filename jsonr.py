import json

f = open("students.json")
students = json.load(f)
f.readline()
f.close()

print(f"Brahvim's marks: {students["Brahvim"]}.")

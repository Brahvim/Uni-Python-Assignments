import json

f = open("files/students.json")
students = json.load(f)
f.readline()
f.close()

print(f"Brahvim's marks: {students["Brahvim"]}.")

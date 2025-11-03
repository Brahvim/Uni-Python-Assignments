print("Please enter three lines of text...!:")
strings = []
record = 0
best = ""

for i in range(3):
    uin = input()
    l = len(uin)

    strings.append(uin + "\n")

    if l > record:
        best = uin

print(f"Largest line: \"{best}\".")
with open("files/uin.txt", "w") as f:
    f.writelines(strings)
    # f.writelines([i + "\n" for i in strings]) # `input()` does NOT record that `\n`!

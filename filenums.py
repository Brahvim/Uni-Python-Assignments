with open("numbers.txt", "w+") as f:
    f.writelines([str(f"{i}\n") for i in range(1, 51)])

    # Use either:
    f.seek(0)
    # with open("numbers.txt", "r") as f:

    print("File contents:")
    print(f.read())
    print("--- End of file contents ---")

# with open("even.txt", "w") as fe, open("numbers.txt", "r") as fn, open("odd.txt", "w") as fo:
# PEP8 supports this formatting!!! Search `help("with")` for `):` **twice** in Python 3.13.5:
with (
        open("odd.txt", "w") as fo,
        open("even.txt", "w") as fe,
        open("numbers.txt", "r") as fn,
):
    for l in fn.readlines():
        if int(l) & 1:
            fo.writelines(l)
        else:
            fe.writelines(l)  # (f"{n}\n") # Slooooooow!

with open("even.txt", "r") as f:
    print(f"Sum of `even.txt` nums: {sum([int(i) for i in f.readlines()])}")

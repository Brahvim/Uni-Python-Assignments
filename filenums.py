with open("files/numbers.txt", "w+") as f:
    f.writelines([str(f"{i}\n") for i in range(1, 51)])

    # Use either:
    f.seek(0)
    # with open("files/numbers.txt", "r") as f:

    print("File contents:")
    print(f.read())
    print("--- End of file contents ---")

# with open("files/even.txt", "w") as fe, open("files/numbers.txt", "r") as fn, open("files/odd.txt", "w") as fo:
# PEP8 supports this formatting!!! Search `help("with")` for `):` **twice** in Python 3.13.5:
with (
        open("files/odd.txt", "w") as fo,
        open("files/even.txt", "w") as fe,
        open("files/numbers.txt", "r") as fn,
):
    for l in fn.readlines():
        if int(l) & 1:
            fo.writelines(l)
        else:
            fe.writelines(l)  # (f"{n}\n") # Slooooooow!

with open("files/even.txt", "r") as f:
    print(
        f"Sum of `files/even.txt` nums: {sum([int(i) for i in f.readlines()])}")

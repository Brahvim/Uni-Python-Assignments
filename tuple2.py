print(f"`sum(1, True, 3.4)` is `{sum((1, True, 3.4))}`.")

try:
    print(f"`sum(1, True, \"a\", 3.4)` is `{sum((1, True, "a", 3.4))}`.")
except Exception:
    print("Cannot add an `str` to numbers!")

# `[:-2]` => `[0:-2]` => `[0:2]` => `[1, 2.2]`
print((1, 2.2, "Hello", "Hi!")[:-2])


def take_inputs(*p_args):
    print(f"Type of `p_args`: `{type(p_args)}`.")
    print(f"Length of `p_args`: `{len(p_args)}`.")


take_inputs(1, 2, 3)

print(sorted((1, 2, 5, 7)))
print(sorted((1, 2, 5, 3.4)))

try:
    print(sorted((1, 2, 5, True, 3.4)))
except:
    pass

try:
    print(sorted((1, 2, 5, True, "a", 3.4)))
except:
    pass

print(tuple(zip((1, 2, 3), ("Ansh", 3.4, "Dhanesh"))))
print(tuple(zip((1, 2, 3), ("Ansh", "Brahvim", "Dhanesh"))))

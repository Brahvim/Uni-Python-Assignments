# Remember what *a call to `list()`* can do:
l = list([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])
l = list("First element!")
l = list(range(10))

l = [x for x in range(10)]
l.insert(-3, 10000)
l.insert(1, -1000)

l.append([0, 1])  # Appends a `list`, not values! # type: ignore

l.extend([2, 3])  # Appends values FROM given `list`.
l.extend((2, 3))  # Other linear structures work, too!

l.remove(5)
e = l.pop()
l.pop(5)
print(l)
print(e)

l.clear()

l = [i for i in range(0x10)]
l.extend(list(i for i in range(0x10)))
print(f"`2` is present `{l.count(2)}` times.")

print(l.index(2))  # Index of first *occurence*.

try:
    print(l.index(-1))
except ValueError:
    pass

l = [i for i in range(5)]
m = list(l)
m.reverse()

print(f"`l`: {m}")
print(f"`l` `list::reverse()`d: {m}")
print(f"`l` reversed via slicing: {l[::-1]}")
print(f"`l` reversed via slicing w/ `len()`: {l[len(l)::-1]}")

m = [
    [x for x in range(2)],
    [x for x in range(2)],
]  # Matrix

print(f"Matrix: `{m}`")
print(f"Matrix, flattened: `{[x for x in m]}`")

# l = [if x % 2 == 0 for x in range(10)] # Bad syntax.
# l = [x for x in range(10) if x % 2 == 0 else 5]  # Bad syntax.
# l = [for x in range(10)]  # Bad syntax.
l = [x for x in range(10) if x % 2 == 0]  # Working syntax.
# l = [for x in range(10) if x % 2 == 0 else 5]  # Bad syntax (if using an `else`, place checks AFTERWARDS).
l = [x if x % 2 == 0 else 5 for x in range(10)]  # Working syntax.
# l = [x if x % 2 == 0 for x in range(10)]  # Bad syntax! Must have `else`...`

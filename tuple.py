# Construction:
t1 = (1,)
t2 = (1, 2)
t3 = 1, 2, True

# del t1, t2, t3

t = tuple((1, 2, 3))

# Extension via `list`:
l = list(t)
l.append(4)
t = tuple(l)

# Extension via tuple:
t = t + (5,)
t += (5,)

print(t)
print(f"Length of `t4`: `{len(t)}`.")

# Search:
print(f"FIRST `5` at: `t4[{t.index(5)}]`")

# Count occurences:
print(f"Times `5` is in tuple `t4`: {t.count(5)}")

# Slicing:
print(t[0])       # First.
print(t[0:2])     # Ist two.
print(t[0:2:2])   # Secondth.
print(t[2:0:-1])  # Reversal.

# Sort:
print("Sort via `list::sort()`:")
l = list(t)
l.sort()
print(tuple(l))

print("Sort via `sorted()`:")
print(sorted(t))

# Lists of tuples:
loT = [t1, t2, t3, t]
loT = [(1, 2), (3,), (4, 5, 6), (7,)]
pairs = [(21, 43), (65, 87), (109, 1211)]

# Looping over them:
for i, j in pairs:
    print(i, j)

# First elements only!:
for i, j in pairs:
    print(i)

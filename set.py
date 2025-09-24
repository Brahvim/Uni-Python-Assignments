s = {}
s = {1, 2, 2, 3}  # Like a `java.util.HashSet`, right?

print(s)  # `[1, 2, 3]` in some order LOL.

try:
    print(s[0])  # Indexing impossible!
except:
    pass

# ...Yeah, no `list::append()` or `list::extend()` here!:
print({2, 3}.union({3, 4}))
print({2, 3}.difference({3, 4}))  # `A - B`! Elements ONLY in `A`!
print({2, 3}.intersection({3, 4}))  # Woohoo!
print({2, 3}.symmetric_difference({3, 4}))  # Elements not in both sets.

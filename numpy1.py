import numpy as np

SZ = 100
arr = np.ones
arr = np.zeros
arr = np.array(SZ, dtype="uint8")
arr = np.arange(9, 7, -1, "uint8")  # [9,7)

print(arr.max())  # Call from object,
print(np.min(arr))  # Call from module if you want!
print(np.sum(arr))
print(np.mean(arr))

mat44 = np.identity(4)  # Makes a 3x3 matrix
print(f"4x4 matrix shape: `{mat44.shape}`.")
print(f"4x4 matrix re-shaped: {mat44.reshape((2, 8))}")

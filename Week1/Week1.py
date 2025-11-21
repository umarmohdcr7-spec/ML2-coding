import numpy as np

n = 10000

X = np.random.randint(0, 2, size = n)

print("First 20 Tosses:", X[:20])
print("The total number of tosses generated:", len(X))
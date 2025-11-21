import numpy as np
# Step 1:
n = 10000

X = np.random.randint(0, 2, size = n)

print("First 20 Tosses:", X[:20])
print("The total number of tosses generated:", len(X))

# Step 2:
running_means = []

for i in range(1, n+1):
    current_mean = np.mean(X[:n])
    running_means.append(current_mean)

print("Running mean at n = 10000: ", running_means[-1] )    

mu_coin = 0.5

deviations = [abs(m-mu_coin) for m in running_means]

print("Deviation at n = 10000", deviations[-1])







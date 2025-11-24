import numpy as np
import matplotlib.pyplot as plt

# Step 1:
n = 10000

X = np.random.randint(0, 2, size = n)

print("First 20 Tosses:", X[:20])
print("The total number of tosses generated:", len(X))

# Step 2: Deviation means how far our calculated mean is from the actual mean that is mu_coin
running_means = []

for i in range(1, n+1):
    current_mean = np.mean(X[:i]) #pay attention how you slice the lists. I used n instead of i before
    running_means.append(current_mean)

print("Running mean at n = 10000: ", running_means[-1] )    

mu_coin = 0.5

deviations = [abs(m-mu_coin) for m in running_means] #abs is predefined python function

print("Deviation at n = 10000", deviations[-1])

# Step 3:
last100_devs= deviations[-100:]
count = 0

for i in last100_devs:
    if i > 0.001:
        count = count + 1

P_n = count/100
print("P_n = ", P_n)

# Plot 1:

plt.figure(figsize=(8,5))
plt.plot(running_means, label="Running Mean $\\bar{X}_n$", color = "blue") # The weird part is used just to make the graph look pretty
plt.axhline(y=mu_coin, color = "red", linestyle="--", label = "True Mean = 0.5") # The task asked to add a line at this point parallel to the x axis

plt.title("Running Sample Mean vs Number of tosses (n)")
plt.xlabel("n(Number of Tosses)")
plt.ylabel("Running Mean")
plt.legend()
plt.grid(True)
plt.savefig("EXP1.1-plot1_mean.png", dpi = 300) # This will save the image

plt.show() # This is used to show what we plotted

# Plot 2:

epsilon = 0.001
plt.figure(figsize=(8,5))
plt.plot(deviations, label="Absolute Deviation $\\delta_n$", color="green") # The weird part is used just to make the graph look pretty
plt.axhline(y=epsilon, color = "red", linestyle="--", label = "epsilon = 0.001") # The task asked to add a line at this point parallel to the x axis

plt.title("Absolute Deviation $\\delta_n$ vs Number of tosses (n) log scale")
plt.xlabel("n(Number of Tosses)")
plt.ylabel("Deviation (log scale)")
plt.legend()
plt.grid(True, which = "both")
plt.savefig("EXP1.1-plot2_deviations.png", dpi = 300)

plt.show()



from collections import deque   # required for efficient moving window

window_size = 100
epsilon = 0.001
sigma = 0.001   # horizontal reference line for the plot

Pn_values = []                  # store P_n values
window = deque(maxlen=window_size)   # sliding window for deviations

# Compute P_n for every n starting from n = 100
for delta in deviations:
    window.append(delta)

    if len(window) == window_size:
        count_exceed = sum(d > epsilon for d in window)   # count deviations > epsilon
        Pn = count_exceed / window_size
        Pn_values.append(Pn)

# ---- Plot 3 ----
plt.figure(figsize=(8,5))
plt.plot(Pn_values, label="$P_n$ (empirical probability)", color="purple")
plt.axhline(y=sigma, color="red", linestyle="--", label="σ = 0.001")

plt.title("Evolution of Empirical Probability $P_n$ vs n")
plt.xlabel("n (starting from 100)")
plt.ylabel("$P_n$")
plt.legend()
plt.grid(True)
plt.savefig("EXP1.1-plot3_Pn.png", dpi=300)

plt.show()
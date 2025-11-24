import numpy as np
import matplotlib.pyplot as plt
import os
os.chdir(os.path.dirname(__file__))  # ensure saving in Week1 folder
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

plt.figure(figsize=(8,5))
plt.plot(running_means, label="Running Mean $\\bar{X}_n$", color = "blue") # The weird part is used just to make the graph look pretty
plt.axhline(y=mu_coin, color = "red", linestyle="--", label = "True Mean = 0.5") # The task asked to add a line at this point parallel to the x axis

plt.title("Running Sample Mean vs Number of tosses (n)")
plt.xlabel("n(Number of Tosses)")
plt.ylabel("Running Mean")
plt.legend()
plt.grid(True)
plt.savefig("plot1_mean.png", dpi = 300) # This will save the image

plt.show() # This is used to show what we plotted

epsilon = 0.001
plt.figure(figsize=(8,5))
plt.plot(running_means, label="Absolute Deviation $\\delta_n$", color = "green") # The weird part is used just to make the graph look pretty
plt.axhline(y=epsilon, color = "red", linestyle="--", label = "epsilon = 0.001") # The task asked to add a line at this point parallel to the x axis

plt.title("Absolute Deviation $\\delta_n$ vs Number of tosses (n) log scale")
plt.xlabel("n(Number of Tosses)")
plt.ylabel("Deviation (log scale)")
plt.legend()
plt.grid(True, which = "both")
plt.savefig("plot2_deviations.png", dpi = 300)

plt.show()
print("Current working directory:", os.getcwd())




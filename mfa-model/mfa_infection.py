import numpy as np
import matplotlib.pyplot as plt

# Parameters
b = 2.0
h = 10.0
Tinf = 5
Timm = 10

maxtime = 30

# Parameter values
St = 0.8
It = 0.2
Rt = 0.0

# Arrays with time points and simulation outcomes
times = np.arange(0,maxtime)
S = []
I = []
R = []

for i in range(maxtime):
    # Add data to data arrays:
    S.append(St)
    I.append(It)
    R.append(Rt)
    # Calculate next step:
    St1 = St - ((8*b*It)/(8*b*It+h))*St + (1.0/Timm)*Rt
    It1 = It + ((8*b*It)/(8*b*It+h))*St - (1.0/Tinf)*It
    Rt1 = Rt + (1.0/Tinf)*It - (1.0/Timm)*Rt
    # Set values to next step:
    St = St1
    It = It1
    Rt = Rt1

# Plot
plt.plot(times, S, 'black', label = "S", lw = 2.0)
plt.plot(times, I, 'red', label = "I", lw = 2.0)
plt.plot(times, R, 'blue', label = "R", lw = 2.0)
plt.legend()
plt.xlabel("Time")
plt.ylabel("Population fraction")
plt.show()

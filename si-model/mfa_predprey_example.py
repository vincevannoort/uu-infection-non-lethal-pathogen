import numpy as np
import matplotlib.pyplot as plt

# Parameters
a = 0.3
b = 0.3
dprey = 0.05
dpred = 0.05

maxtime = 200

# Initial values of prey and predator
Rt = 0.2
Nt = 0.1

# Arrays with time points and simulation outcomes
times = np.arange(0,maxtime)
R = []
N = []

for i in range(maxtime):
    # Add data to data arrays:
    R.append(Rt)
    N.append(Nt)
    # Calculate next step:
    Rt1 = Rt + a*Rt*(1-Rt-Nt) - dprey*Rt - b*Rt*Nt
    Nt1 = Nt + b*Rt*Nt - dpred*Nt
    # Set values to next step:
    Rt = Rt1
    Nt = Nt1

# Plot
plt.plot(times, R, 'black', lw = 2.0)
plt.plot(times, N, 'red', lw = 2.0)
plt.xlabel("Time")
plt.ylabel("Prey density (black) and Predator density (red)")
plt.show()

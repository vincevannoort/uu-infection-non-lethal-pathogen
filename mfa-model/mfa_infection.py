import numpy as np
import matplotlib.pyplot as plt

# Parameters
b = 1.0
Tinf = 200
Timm = 600

# Scaling parameter
# h = 10.0

maxtime = 1000

# Parameter values
St = 0.98
It = 0.01
Rt = 0.01

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
    
    # Exponential definition of infection probability
    St1 = St - (1 - np.exp(-8*b*It*0.01))*St + (1.0/Timm)*Rt
    It1 = It + (1 - np.exp(-8*b*It*0.01))*St - (1.0/Tinf)*It
    
    # Scaling parameter definition of infection probability
# =============================================================================
#     St1 = St - ((8*b*It)/(8*b*It+h))*St + (1.0/Timm)*Rt
#     It1 = It + ((8*b*It)/(8*b*It+h))*St - (1.0/Tinf)*It
# =============================================================================
    
    Rt1 = Rt + (1.0/Tinf)*It - (1.0/Timm)*Rt
    
    # Set values to next step:
    St = St1
    It = It1
    Rt = Rt1

# Plot
plt.plot(times, S, 'black', label = "S", lw = 2.0)
plt.plot(times, I, 'red', label = "I", lw = 2.0)
plt.plot(times, R, 'blue', label = "R", lw = 2.0)
plt.title("Infection duration: " + str(Tinf) + ", Immunity duration: " + str(Timm))
plt.legend()
plt.xlabel("Time")
plt.ylabel("Population fraction")
plt.show()

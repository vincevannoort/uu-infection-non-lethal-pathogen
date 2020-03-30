import numpy as np
import matplotlib.pyplot as plt

# Parameters
b = 1.0
h = 10.0
Tinf1 = 5
Tinf2 = 12
Timm = 10

maxtime = 80

# Parameter values
St = 0.8
I1t = 0.1
I2t = 0.1
Rt = 0.0

# Arrays with time points and simulation outcomes
times = np.arange(0,maxtime)
S = []
I1 = []
I2 = []
R = []

for i in range(maxtime):
    # Add data to data arrays:
    S.append(St)
    I1.append(I1t)
    I2.append(I2t)
    R.append(Rt)
    # Calculate next step:
    St1 = St - ((8*b*I1t)/(8*b*I1t+h))*St - ((8*b*I2t)/(8*b*I2t+h))*St + (1.0/Timm)*Rt
    I1t1 = I1t + ((8*b*I1t)/(8*b*I1t+h))*St - (1.0/Tinf1)*I1t
    I2t1 = I2t + ((8*b*I2t)/(8*b*I2t+h))*St - (1.0/Tinf2)*I2t
    Rt1 = Rt + (1.0/Tinf1)*I1t + (1.0/Tinf2)*I2t - (1.0/Timm)*Rt
    # Set values to next step:
    St = St1
    I1t = I1t1
    I2t = I2t1
    Rt = Rt1

# Plot
plt.plot(times, S, 'black', label = "S", lw = 2.0)
plt.plot(times, I1, 'red', label = "I1", lw = 2.0)
plt.plot(times, I2, 'green', label = "I2", lw = 2.0)
plt.plot(times, R, 'blue', label = "R", lw = 2.0)
plt.legend()
plt.xlabel("Time")
plt.ylabel("Population fraction")
plt.show()

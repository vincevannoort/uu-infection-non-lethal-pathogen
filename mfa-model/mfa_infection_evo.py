import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import time

# Colors
color_dict = {
    'Infected 1': '#ff5e5e',
    'Infected 2': '#b03bc5',
    'Susceptible': '#eeeeee',
    'Recovered': '#ffeb3b'
}

# Parameters
b = 1.0
h = 10.0
Tinf1 = 70
Tinf2 = 500
Timm = 300

maxtime = 400

# Parameter values
St = 0.98
I1t = 0.005
I2t = 0.005
Rt = 0.01

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
    St1 = St - (1 - np.exp(-8*b*I1t*0.01))*St - (1 - np.exp(-8*b*I2t*0.01))*St + (1.0/Timm)*Rt
    I1t1 = I1t + (1 - np.exp(-8*b*I1t*0.01))*St - (1.0/Tinf1)*I1t    
    I2t1 = I2t + (1 - np.exp(-8*b*I2t*0.01))*St - (1.0/Tinf2)*I2t

# =============================================================================
#     St1 = St - ((8*b*I1t)/(8*b*I1t+h))*St - ((8*b*I2t)/(8*b*I2t+h))*St + (1.0/Timm)*Rt
#     I1t1 = I1t + ((8*b*I1t)/(8*b*I1t+h))*St - (1.0/Tinf1)*I1t
#     I2t1 = I2t + ((8*b*I2t)/(8*b*I2t+h))*St - (1.0/Tinf2)*I2t
# =============================================================================
    
    Rt1 = Rt + (1.0/Tinf1)*I1t + (1.0/Tinf2)*I2t - (1.0/Timm)*Rt
    # Set values to next step:
    St = St1
    I1t = I1t1
    I2t = I2t1
    Rt = Rt1

# Plot
data = pd.DataFrame(data={ 'Infected 1': I1, 'Infected 2': I2, 'Susceptible': S, 'Recovered': R })
color = [color_dict.get(x, '#333333') for x in data.columns]
title =  f'Infection duration 1: {Tinf1}, Infection duration 2: {Tinf2}'
data.plot.area(color=color, title=title, lw=3).legend(loc='upper right')
plt.margins(0)
plt.xlabel('Time')
plt.ylabel('Population fraction')
start_time = time.strftime("%Y%m%d-%H%M%S")
plt.savefig(f'figures/Tinf1{Tinf1}-Tinf2{Tinf2}-Timm{Timm}.pdf')
# plt.title("Infection duration 1: " + str(Tinf1) + ", Infection duration 2: " + str(Tinf2))
# plt.legend(loc = "upper right")
# plt.xlabel("Time")
# plt.ylabel("Population fraction")
# plt.show()

St = 0.7
It = 0.2

Tinf = np.linspace(20,200,100)
pcgr = ((1 - np.exp(-8*b*It*0.01))/It)*St - (1.0/Tinf)

plt.plot(Tinf,pcgr, 'blue')
plt.xlabel("Infection Duration")
plt.ylabel("Growth Rate")
plt.title("Per Capita Growth Rate vs Infection Duration")






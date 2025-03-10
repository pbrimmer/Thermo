import numpy as np
import matplotlib.pyplot as plt
import sys

def P_VDW(Vr,Tr):
    
    Pr = 8.0*Tr/(3.0*Vr - 1.0) - 3.0/(Vr*Vr)

    return Pr

Vr = np.arange(0.5,3.01,0.01) #Which is V/Vc

Tr = np.arange(0.85,1.2,0.05)               #Needs to be reasonably close to the critical temperature.

plt.xlim(0.5,3.0)
plt.ylim(0.0,5.0)

for i in range(len(Tr)):
    plt.plot(Vr,P_VDW(Vr,Tr[i]))

plt.show()

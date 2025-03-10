import numpy as np
import matplotlib.pyplot as plt
import sys


#Peng & Robinson 1976

def P_PR(v,T):

    #For water:

    R = 8.314           #Gas constant, J/(mol K)

    Tc = 647.3          #Critical temperature (K)
    Pc = 221.2*1e5               #Critical pressure (Pa)
    omega = 0.344       #Acentric constant

    kappa = 0.37464 + 1.54226*omega - 0.26992*omega*omega

    alpha = (1.0 + kappa*(1.0 - (T/Tc)**0.5))**2.0

    a = 0.45724*R*R*Tc*Tc/Pc*alpha
    b = 0.0778*R*Tc/Pc
  
    print(a)
    print(b)

    for i in range(len(v)):
        if v[i] <= 1.1*b: v[i] = 1.1*b
        P = R*T/(v - b) - a/(v*(v+b) + b*(v-b))

    print(P)
    print(R*T/(v - b))

    return P

#v = np.arange(1e-5,1e-3+1e-5,1e-5) #Molar volume in m3 mol-1
v = np.logspace(-5.0,1.0,num=500)

plt.xscale('log')
plt.yscale('log')

#v *= 1e-6

T = 373.0

#plt.xlim(0.5,3.0)
plt.ylim(1e3,1e8)

plt.plot(v,P_PR(v,T))

plt.show()

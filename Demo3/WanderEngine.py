import numpy as np
import matplotlib.pyplot as plt

#Choose a path:

def path(P0,V0,t):

    #Some parametric function of pressure and volume.
    #the example is set such that volume decreases and pressure increases adiabatically.
    
    gamma = 5.0/3.0

    V = V0/t
    P = P0*t**gamma
    V = V0*t
    P = P0*t**(-gamma)

    return P,V

k = 1.3806e-23      #Boltzmann constant, J/K

t0 = 1.0            #Starting for the parameter, for paramaterized p,V
t1 = 10.0            #Ending for the parameter, for paramaterized p,V
dt = 1e-4       #Stepsize for t

#Starting point:

S0 = 0.0         #Entropy at starting point (arbitarily set to zero, J/K)
T0 = 300.0       #Starting Temperature in K
P0 = 1e5         #Starting Pressure in Pa
V0 = 1.0         #Starting Volume, in m3

N0 = P0*V0/(k*T0)       #Solve for starting N, not independent
N = N0

U0 = 1.5*N*k*T0        #Starting internal energy, naturally set 3/2 N k T
Q0 = 0.0        #Starting heat, naturally set to zero (J)
W0 = 0.0        #Starting work, naturally set to zero (J)

t = np.arange(t0,t1+dt,dt)

P,V = path(P0,V0,t)

plt.plot(V,P,'k-')
plt.savefig('./Phase-Path.pdf',bbox_inches='tight')

S = S0
T = T0
U = U0
Q = Q0
W = W0

for i in range(len(t)-1):
    dP = P[i+1] - P[i]
    dV = V[i+1] - V[i]

    dS = 2.5*N*k/V[i+1] * dV + 1.5*N*k/P[i+1] * dP
    dT = (P[i+1] * dV + V[i+1] * dP)/(N*k)
    dU = 1.5*N*k*dT
    dW = -P[i+1] * dV

    S += dS
    T += dT

    dQ = T * dS

    U += dU
    Q += dQ
    W += dW

print('Volume change = ' + ('%.3e' % (V[len(P)-1] - V[0])) + ' m3')
print('Pressure change = ' + ('%.3e' % (P[len(P)-1] - P[0])) + ' Pa')
print('----------')
print('Starting Temperature = ' + ('%.2f' % T0) + ' K')
print('Temperature change = ' + ('%.2f' % (T-T0)) + ' K')
print('Final Temperature = ' + ('%.2f' % T) + ' K')
print('----------')
print('Starting Internal Energy = ' + ('%.3e' % U0) + ' J')
print('Change in Internal Energy = ' + ('%.3e' % (U - U0)) + ' J')
print('Change in Entropy = ' + ('%.3e' % S) + ' J/K')
print('Change in Heat = ' + ('%.3e' % Q) + ' J')
print('Change in Work = ' + ('%.3e' % W) + ' J')
print('----------')
print('Test for dU = dQ + dW:')
print('dU - dQ - dW = ' + ('%.3e' % (U - U0 - Q - W)) + ' J')

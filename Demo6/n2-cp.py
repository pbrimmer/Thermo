#Heat Capacity at Contant Pressure of N2
#Based on https://webbook.nist.gov/cgi/cbook.cgi?ID=C7727379&Mask=1#Thermo-Gas
#Try to extend this to higher temperature!

import numpy as np
import matplotlib.pyplot as plt

R = 8.314           #Ideal gas constant, in J/(K mol)

#Parameters for cp
A = 28.98641
B = 1.853978
C = -9.647459
D = 16.63537
E = 0.000117

T = np.arange(100.0,500.01,0.01)
t = T/1000.0
#cp in units of J/(K mol)
Cp = A + B*t + C*t*t + D*t*t*t + E/t/t
plt.plot(T,Cp,'k-')
plt.plot(T,3.5*R*T**0.0,'k--')
plt.plot(T,4.5*R*T**0.0,'k:')

A = 19.50583
B = 19.88705
C = -8.598535
D = 1.369784	
E = 0.527601

T = np.arange(500.0,2000.01,0.01)
t = T/1000.0
#cp in units of J/(K mol)
Cp = A + B*t + C*t*t + D*t*t*t + E/t/t
plt.plot(T,Cp,'k-',label='NIST')
plt.plot(T,3.5*R*T**0.0,'k--',label='$3.5R$')
plt.plot(T,4.5*R*T**0.0,'k:',label='$4.5R$')

#A = 35.51872
#B = 1.128728
#C = -0.196103
#D = 0.014662
#E = -4.553760

#T = np.arange(2000.0,6000.01,0.01)
#t = T/1000.0
#cp in units of J/(K mol)
#Cp = A + B*t + C*t*t + D*t*t*t + E/t/t
#plt.plot(T,Cp,'k-')
#plt.plot(T,3.5*R*T**0.0,'k--')
#plt.plot(T,4.5*R*T**0.0,'k:')

plt.title('N$_2$ specific heat')

plt.xlabel('temperature (K)')
plt.ylabel('$c_p$ (J/(mol K))')

plt.legend()
plt.savefig('./N2-CP.pdf',bbox_inches='tight')

import numpy as np
import matplotlib.pyplot as plt

#Two state system, E0 = 0, E1 = E:

E = 1.0

beta = np.arange(0.0,10.01,0.01)

Z = 1.0 + np.exp(-beta*E)

plt.xlabel(r'$\beta$')
plt.ylabel(r'$Z$')

plt.plot(beta,Z)

plt.show()
plt.clf()

plt.xlabel(r'$\beta$')
plt.ylabel(r'probability')

plt.plot(beta,1.0/Z,'r-',label='$p(0)$')
plt.plot(beta,np.exp(-beta*E)/Z,'b--',label=r'$p(\epsilon)$')


plt.legend()
plt.show()

plt.clf()

Eav = E*np.exp(-beta*E)/Z

plt.plot(beta,Eav,'k-')
plt.xlabel(r'$\beta$')
plt.ylabel(r'$<E>$')

plt.show()
plt.clf()

Fluct = E*E*np.exp(-beta*E)/(Z*Z)

plt.plot(beta,Fluct,'k-')
plt.xlabel(r'$\beta$')
plt.ylabel(r'$(\Delta E)^2$')

plt.show()

plt.clf()

plt.xlim(0.0,3.0)
plt.ylim(0.0,5.0)

plt.plot(beta,(Fluct/(Eav*Eav))**0.5,'k-')
plt.xlabel(r'$\beta$')
plt.ylabel(r'$(\Delta E)/<E>$')

plt.show()

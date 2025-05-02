#ULTRAVIOLET CATASTROPHE!!!!

import numpy as np
import matplotlib.pyplot as plt

x = np.arange(1.0,10000.1,0.1) #Wavelength in Angstroms

#Can you fix the ultraviolet catastrophe?

kB = 1.38e-23        #Boltzmann constant in J/K
T = 300.0           #Temperature in K
c = 3.0e8           #speed of light in m/s

xm = x*1e-10

I = 2.0*c*kB*T/(xm*xm*xm*x)

plt.xlabel('wavelength ($\AA$)')
plt.ylabel('spectral irradiance (W m$^{-2}$ $\AA^{-1}$)')

plt.yscale('log')
plt.plot(x,I,'k-')
plt.savefig('./SpectralIrradiance.pdf',bbox_inches='tight')

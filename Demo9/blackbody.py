import numpy as np
import matplotlib.pyplot as plt

def Blambda (x, T, Rstar, a):
    glambda = 1.191e20/(x*x*x*x*x)      #The leading term, density of states times hc/lambda
    weight = 1.0/(np.exp(1.439e7/(x*T)) - 1.0) #Weight, from the partition function.

    return glambda*weight*Rstar*Rstar/(a*a)*2.162e-5*np.pi

x, I = np.loadtxt('modern-solar.dat',usecols=(0,1),skiprows=1,unpack=True)

x /= 10.0       #angstrom to nm
I *= 1.986e-11/x    #cm-2 s-1 A-1 to W m-2 nm-1

plt.xlim(200.0,1000.0)

plt.plot

plt.plot(x,I,'k-',lw=0.7)
plt.plot(x,Blambda(x,6000.0,1.0,1.0),'m:',lw=1.5)
plt.plot(x,Blambda(x,5872.0,1.0,1.0),'b-.',lw=1.5)
plt.plot(x,Blambda(x,5772.0,1.0,1.0),'g--',lw=1.5)
plt.plot(x,Blambda(x,5472.0,1.0,1.0),'y-.',lw=1.5)
plt.plot(x,Blambda(x,4700.0,1.0,1.0),'r:',lw=1.5)
plt.show()

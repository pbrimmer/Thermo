import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_color_codes()

xi = np.arange(0.0001,0.9999,0.0001)

K = (2.0*xi)**2.0/((1.0-xi)*(10.0 - 3.0*xi)**3.0)

plt.xscale('log')
plt.yscale('log')
plt.plot(K,2.0*xi + 1.0-xi + 10.0-3.0*xi,'k-',lw=3,label='total pressure')
plt.plot(K,1.0-xi,'b-',lw=2,label='N$_2$')
plt.plot(K,10.0-3.0*xi,'r--',lw=2,label='H$_2$')
plt.plot(K,2.0*xi,'g-.',lw=2,label='NH$_3$')

plt.tick_params(axis='both', which='major',
                labelsize=13, length=6, width=1.5)

plt.tick_params(axis='both', which='minor',
                length=3, width=1)

plt.xlabel(r'$K_{\rm eq}$',fontsize=14)
plt.ylabel(r'pressure (bar)',fontsize=14)

plt.legend(loc='upper left', bbox_to_anchor=(1.02, 1), borderaxespad=0.)
plt.savefig('./Equilibrium.pdf',bbox_inches='tight')

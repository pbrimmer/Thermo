import numpy as np
import matplotlib.pyplot as plt

import seaborn as sns
sns.set_color_codes()

const1 = np.arange(10.0,100.0,10.0)
const2 = np.arange(3.0,30.0,3.0)
V = np.arange(0.1,10.1,0.1)
gamma = 5.0/3.0

plt.xlim(0.0,8.0)
plt.ylim(0.0,7.0)

plt.xlabel('Volume')
plt.ylabel('Pressure')

plt.text(5.1,5.1,'Adiabat',color='b',fontsize=13,rotation=-52)
plt.text(1.0,1.0,'Isotherm',color='r',fontsize=13,rotation=-35)

for i in range(len(const1)):
    Pada = const1[i]/(V**gamma)
    plt.plot(V,Pada,'b-',lw=1.5)

for i in range(len(const2)):
    Piso = const2[i]/V
    plt.plot(V,Piso,'r-',lw=2.0)
plt.savefig('IsothermAdiabat.pdf',bbox_inches='tight')


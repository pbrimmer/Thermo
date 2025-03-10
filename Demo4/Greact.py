import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

#Write out a reaction here using '+' to separate species, and '->' to separate reactants and products.

reaction = 'H2O -> HO + H'
#reaction = 'H2S + H2S + CO2 -> CS2 + H2O + H2O'
#reaction = 'OCS + S -> CO + S2'
#reaction = 'HCN + HCN + HCN + HCN + O2 + O2 + O2 + O2 + O2 -> H2O + H2O + CO2 + CO2 + CO2 + CO2 + N2 + N2'
#reaction = 'HCN -> HNC'
#reaction = 'H2 + H2 + H2 + CO -> CH4 + H2O'
#reaction = 'N2 + H2 + H2 + H2 -> H3N + H3N'
#reaction = 'CH4 + O2 + O2 -> CO2 + H2O + H2O'

R = 8.3145e-3            #Gas constant, units of kJ/(mol K)

#Temperature range, plotted from 100 K -- 3000K

T = np.arange(1600.0,2200.1,0.1)

#Reads cond_initial.dat from update-species, which should always be identical to the cond_initial.dat from the cond_initial folder!

Bulk = np.genfromtxt('./reaction-list/update-species/cond_initial.dat',skip_header=10,dtype=str)

#Parses the reaction:

twosides = reaction.split('->')

reactants = twosides[0]
products = twosides[1]

reactant = np.array(reactants.split('+'))
product = np.array(products.split('+'))

for i in range(len(reactant)):
    reactant[i] = reactant[i].strip()

for i in range(len(product)):
    product[i] = product[i].strip()

#Output to make sure this is producing what you want
print('Reaction:')
print(reaction)
print('-------')
print('Reactants:')
print(reactants)
print('Products:')
print(products)

areact = np.zeros(14)
aprod = np.zeros(14)

count = 0
ctot = len(product) + len(reactant)
for j in range(len(reactant)):
    for i in range(len(Bulk)):
        species = Bulk[i,1]         #Species name

    #Reading off the cond_initial values for the thermodynamic quantities (Nasa 7-th order
    #polynomials. Check to make sure species names match. Replace 'D' with 'e' and sum values.
        if species == reactant[j]:
            areact += (np.char.replace(Bulk[i,19:33],'D','e')).astype(float)
            print(species)
            print(Bulk[i,19:33])
            count += 1
    
for j in range(len(product)):
    for i in range(len(Bulk)):
        species = Bulk[i,1]         #Species name

        if species == product[j]:
            aprod += (np.char.replace(Bulk[i,19:33],'D','e')).astype(float)
            count += 1

#If some species is included in the reaction that is not in the cond_initial file, flags the error
if count != ctot: print('Error! Some species in reaction is not in cond_initial.dat!')

#Greact and Gprod (kJ/mol) when T > 1000 K
Greact1 = R*T*(areact[0]*(1.0 - np.log(T)) - 0.5*areact[1]*T - 0.166667*areact[2]*T*T - 0.083333*areact[3]*T*T*T - 0.05*areact[4]*T*T*T*T + areact[5]/T - areact[6])
Gprod1 = R*T*(aprod[0]*(1.0 - np.log(T)) - 0.5*aprod[1]*T - 0.166667*aprod[2]*T*T - 0.083333*aprod[3]*T*T*T - 0.05*aprod[4]*T*T*T*T + aprod[5]/T - aprod[6])

#Greact and Gprod (kJ/mol) when T < 1000 K
Greact2 = R*T*(areact[7]*(1.0 - np.log(T)) - 0.5*areact[8]*T - 0.166667*areact[9]*T*T - 0.083333*areact[10]*T*T*T - 0.05*areact[11]*T*T*T*T + areact[12]/T - areact[13])
Gprod2 = R*T*(aprod[7]*(1.0 - np.log(T)) - 0.5*aprod[8]*T - 0.166667*aprod[9]*T*T - 0.083333*aprod[10]*T*T*T - 0.05*aprod[11]*T*T*T*T + aprod[12]/T - aprod[13])

#Constructs a Greact + Gprod that are valid over the full range.
Greact = np.zeros(len(Greact1))
Gprod = np.zeros(len(Gprod1))

for i in range(len(Greact)):
    if T[i] > 1000.0:
        Greact[i] = Greact1[i]
        Gprod[i] = Gprod1[i]
    if T[i] <= 1000.0:
        Greact[i] = Greact2[i]
        Gprod[i] = Gprod2[i]

#Plots the values.
plt.title(reaction)
plt.plot(T,Gprod - Greact)

plt.xlabel('temperature (K)')
plt.ylabel('Gibbs free energy (kJ/mol)')

plt.savefig('./out/Figures/Gr-kJ_mol.pdf',bbox_inches='tight')

fout = open('./out/Gr-kJ_mol.dat','w')

fout.write('Reaction energetics (Gibbs free energy, kJ/mol) as a function of temperature (K).')
fout.write('\n------------------------------------------------------------------------------')
fout.write('\nREACTION: ' + reaction)
fout.write('\n------------------------------------------------------------------------------')
fout.write('\n\n T(K)    Greactants(kJ/mol)     Gproducts(kJ/mol)      Gr (kJ/mol)       Keq')

for i in range(len(T)):
    fout.write('\n   ')
    fout.write('%.2f' % T[i])
    fout.write('   ')
    fout.write('%.3e' % Greact[i])
    fout.write('   ')
    fout.write('%.3e' % Gprod[i])
    fout.write('   ')
    fout.write('%.3e' % (Gprod[i] - Greact[i]))
    fout.write('   ')
    fout.write('%.3e' % (np.exp((-Gprod[i] + Greact[i])/(R*T[i]))))
    
    
fout.close()

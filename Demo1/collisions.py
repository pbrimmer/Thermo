import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import imageio
import sys

N = 500            #Number of particles (integer)
#N = 50
R = 1.0           #Radius of particles
L = 100.0         #Length of box (area = L*L)

vstart = 1.0    #Starting velocity for all particles.

ti = 0.0         #Starting time
tf = 500.0       #Ending time
dt = 1.0        #Timestep

delta = R*0.1

#Set all positions and velocities = (0,0)
x = np.zeros((N,2))
v = np.zeros((N,2))

vmodnow = np.zeros(N)

#Randomize positions and velocities
for i in range(N):
    x[i,0] = np.random.uniform(2.0*R,L-2.0*R)
    x[i,1] = np.random.uniform(2.0*R,L-2.0*R)
    v[i,0] = np.random.uniform(-1.0,1.0)
    v[i,1] = np.random.uniform(-1.0,1.0)
    Diff = vstart/np.sqrt(v[i,0]**2.0 + v[i,1]**2.0)
    v[i,0] *= Diff
    v[i,1] *= Diff
    #if x[i,1] > 0.5*L: x[i,0] = L-2.0*R
    #if x[i,1] <= 0.5*L: x[i,0] = 2.0*R
    #if v[i,1] > 0.0: v[i,0] = 1.0
    #if v[i,1] <= 0.0: v[i,0] = -1.0
    #v[i,0] = 0.0


for i in range(N):
    vmodnow[i] = np.sqrt(v[i,0]*v[i,0] + v[i,1]*v[i,1])

vmod = np.array([vmodnow])

t = ti          #initiate the time

#Set up the plot animation
fig, ax = plt.subplots()

count = 0

images = []

while t < tf:
    for i in range(N):
        x[i,0] += v[i,0]*dt
        x[i,1] += v[i,1]*dt

        #Wall collision:
        #Horizontal wall:
        if x[i,0] - R <= 0.0:
            x[i,0] = R
            v[i,0] = -v[i,0]

        if x[i,0] + R >= L:
            x[i,0] = L - R
            v[i,0] = -v[i,0]

        #Vertical wall:
        if x[i,1] - R <= 0.0:
            x[i,1] = R
            v[i,1] = -v[i,1]

        if x[i,1] + R >= L:
            x[i,1] = L - R
            v[i,1] = -v[i,1]


    #No ballclip after collision:
    for i in range(N):
        for j in range(N):
            rij = np.sqrt((x[i,0] - x[j,0])**2.0 + (x[i,1] - x[j,1])**2.0)
            if rij <= 2.0*R and i != j:
                rvdot = (v[i,0] - v[j,0])*(x[i,0]-x[j,0]) + (v[i,1] - v[j,1])*(x[i,1]-x[j,1])
                rrdot = (x[i,0] - x[j,0])*(x[i,0]-x[j,0]) + (x[i,1] - x[j,1])*(x[i,1]-x[j,1])
                v[i,0] = v[i,0] - rvdot*(x[i,0] - x[j,0])/rrdot
                v[i,1] = v[i,1] - rvdot*(x[i,1] - x[j,1])/rrdot
                v[j,0] = v[j,0] - rvdot*(x[j,0] - x[i,0])/rrdot
                v[j,1] = v[j,1] - rvdot*(x[j,1] - x[i,1])/rrdot
                
                alpha = R - 0.5*rij + delta
                x[j,0] = x[j,0] + (x[j,0] - x[i,0])*alpha/rij
                x[j,1] = x[j,1] + (x[j,1] - x[i,1])*alpha/rij
                x[i,0] = x[i,0] - (x[j,0] - x[i,0])*alpha/rij
                x[i,1] = x[i,1] - (x[j,1] - x[i,1])*alpha/rij

    vmodnow = np.zeros(N)
    for i in range(N):
        vmodnow[i] = np.sqrt(v[i,0]*v[i,0] + v[i,1]*v[i,1])

    vmod = np.append(vmod,[vmodnow],axis=0)

    plt.cla()
    plt.axis('equal')
    ax.set_aspect('equal', adjustable='box')
    conv = 6.0
    ax.set_xlim([0, L])
    ax.set_ylim([0, L])
    ax.plot(x[:,0],x[:,1],'bo',ms=R*conv)
    #fig.canvas.draw()
    #plt.pause(0.1)
    plt.savefig('./Animation.png')

    images.append(imageio.imread('./Animation.png'))

    t += dt

    print('t/tf = ' + ('%.4f' % (t/tf))) 
    count += 1

imageio.mimsave('movie.gif',images)

plt.clf()

vth = np.arange(0.0,3.001,0.001)
a = 2.0/(1.0**2.0)
fvth = a*vth*np.exp(-a*vth**2.0/(2.0))

himages = []

for i in range(len(vmod)):
    plt.cla()
    plt.xlim(0.0,3.0)
    plt.ylim(0.0,2.0)
    plt.plot(vth,fvth,'k-')

    plt.hist(vmod[i],bins=30,range=(0.,3.),density=True)
    plt.savefig('Histogram.png')
    himages.append(imageio.imread('./Histogram.png'))

imageio.mimsave('hist-movie.gif',himages)

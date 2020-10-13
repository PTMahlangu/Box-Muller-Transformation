import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
from scipy.stats import rayleigh

#______________________NO: OF SMAPLES_____________________________
npoints = 10000
#_______________________Box–Muller transform______________________
u1 = np.random.random(npoints)
u2 = np.random.random(npoints)
#                       Z1 & Z2 Normal distribution
#z1 = np.sqrt(-2.0*np.log(u1)) * np.cos(2*np.pi*u2) 
#z2 = np.sqrt(-2.0*np.log(u1)) * np.sin(2*np.pi*u2)
z1 = np.sqrt(-2.0*np.log(u1)) 

#______________________Rayleigh Distribution______________________
#ray = np.sqrt(z1**2+z2**2)
ray = 1 * z1
#______________________Plotting Distributions______________________
plt.hist(ray, bins=50, normed=1, alpha=0.5, linewidth=0, color='blue')
#plt.hist(z1, bins=50, normed=1, alpha=0.5, linewidth=0, color='green') 
#plt.hist(z2, bins=50, normed=1, alpha=0.5, linewidth=0, color='yellow')

#______________________Line OF FIT _______________________________
x = np.linspace(-4,4,100)
#plt.plot(x, norm.pdf(x))
plt.plot(x, rayleigh.pdf(x))

import numpy as np	
import matplotlib.pyplot as plt
from matplotlib import rc

plt.rcParams.update({'font.size': 22})
plt.rcParams["figure.figsize"] = (16,10)
plt.rcParams['text.usetex'] = True

rc('font',**{'family':'serif','serif':['Palatino']})


file1 = np.loadtxt("Ar_CO2_90_10_0.8cm.txt")  
x1 = file1[:,0]
y1 = file1[:,1]
plt.plot(x1, y1, label='Ar/CO$_{2}$ (90/10) - 0.8\,cm drift region', color ="red")

file2 = np.loadtxt("Ar_CO2_90_10_3cm.txt")  
x2 = file2[:,0]
y2 = file2[:,1]
plt.plot(x2, y2, label='Ar/CO$_{2}$ (90/10) - 3.0\,cm drift region')


file3 = np.loadtxt("Kr_CO2_90_10_0.8cm.txt")  
x3 = file3[:,0]
y3 = file3[:,1]
plt.plot(x3, y3, label='Kr/CO$_{2}$ (90/10) - 0.8\,cm drift region', color ="green")

file4 = np.loadtxt("Pure_neon_0.8.txt")  
x4 = file4[:,0]
y4 = file4[:,1]
plt.plot(x4, y4, label='Pure Ne - 0.8\,cm drift region', color ="magenta")



plt.xlabel('Photon Energy (eV)')
plt.ylabel('Efficiency', fontsize =26)
plt.legend(prop={'size': 17.5})
plt.draw()

plt.savefig('quantumEff.pdf')

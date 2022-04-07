import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from matplotlib import rc


plt.rcParams.update({'font.size': 22})
plt.rcParams["figure.figsize"] = (10,10)
plt.rcParams['text.usetex'] = True
plt.rcParams["legend.loc"] = 'best' 

rc('font',**{'family':'serif','serif':['Palatino']})



f= np.loadtxt('0.3GeV_400Vcm_1cm_total.txt', unpack='False')
f2= np.loadtxt('1GeV_400Vcm_1cm_total.txt', unpack='False')
f3= np.loadtxt('10GeV_400Vcm_1cm_total.txt', unpack='False')

bins = np.linspace(10, 510, 100)
plt.hist(f, bins=bins, alpha=0.5, label="0.3 GeV", density=True)
plt.hist(f2, bins=bins, alpha=0.5, label="1.0 GeV", density=True)
plt.hist(f3, bins=bins, alpha=0.5, label="10 GeV", density=True)

plt.xlabel('Number of Electrons')
plt.ylabel('Entries')
plt.xscale('log')
plt.title('Muon energy loss in Ar/CO$_{2}$(70/30) - 1cm')
plt.legend()
plt.show()

import numpy as np
import matplotlib
from matplotlib import pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import math

myAxisLabelSize=32
myTickLabelSize=24
myLegendLabelSize=24
myTitleSize=30

data = np.genfromtxt("VaryBeamEnergy.dat")

coatingNoise = data[:,5]
r_0 = data[:,0]*250.e-6/np.sqrt(2)
kB = 1.3806488e-23
T = 300.
f = 100.
wm = data[:,0]*250.e-6
sigmaSub = 0.17
YoungModSub = 72.e9
phiCoat = 1.e-6
phiSub = 1.e-6
d = 6.83e-6
YoungModCoat = 72.e9
sigmaCoat = 0.17
R = 12500.e-6


# This is equation 43 in the paper.
analytic = np.sqrt((2*kB*T/((math.pi**2)*f))*((1-(sigmaSub**2))/(wm*YoungModSub))*(d/wm)*((phiCoat)/(YoungModSub*YoungModCoat*(1-sigmaCoat**2)*(1-sigmaSub**2)))*(YoungModCoat**2*(1+sigmaSub)**2*(1-2*sigmaSub)**2+YoungModSub**2*(1+sigmaCoat)**2*(1-2*sigmaCoat)))

print analytic,coatingNoise/np.sqrt(f)
fig = plt.gcf()
ax = plt.gca()

gridwidth=0.5
gridcolor=(0.8,0.8,0.8)

#ax.plot(d/r_0, analytic, marker='None', label='Approx. analytic', color='b', linestyle='dashed')
#ax.plot(d/r_0, coatingNoise/np.sqrt(f), marker='D', label='Numerical', color='k')
ax.plot(d/r_0, np.abs(analytic-coatingNoise/np.sqrt(f))/analytic, marker='D', label='', color='k')
ax.set_yscale('log')
ax.set_xscale('log')
#ax.set_ylim([5.9e-19,6.9e-19])
ax.set_xlabel('$d/r_0$', fontsize=myAxisLabelSize)
ax.set_ylabel(r'$\left|\frac{\mathrm{analytic-numerical}}{\mathrm{analytic}}\right|$', fontsize=myAxisLabelSize)
ax.tick_params(axis='x', labelsize=myTickLabelSize, pad=12, length=10)
ax.tick_params(which='minor', length=5)
ax.tick_params(axis='y', labelsize=myTickLabelSize, length=10)
#ax.set_title('F. silica coat noise diff', fontsize=myTitleSize, color='k', y=1.04)
ax.grid(b=True, which='major', color=gridcolor, linestyle='solid', linewidth=gridwidth)
#ax.legend(loc='best', fontsize=myLegendLabelSize)

fig.tight_layout()
pdf = PdfPages('VaryBeamNoiseDiff.pdf')
pdf.savefig()
pdf.close()



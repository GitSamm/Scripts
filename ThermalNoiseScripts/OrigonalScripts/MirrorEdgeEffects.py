import numpy as np
import matplotlib
from matplotlib import pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import math

myAxisLabelSize=32
myTickLabelSize=24
myLegendLabelSize=24
myTitleSize=32

data = np.genfromtxt("VaryMirrorEnergy.dat")

coatingNoise = data[:,5]
r_0 = 250.e-6/np.sqrt(2)
kB = 1.3806488e-23
T = 300.
f = 100.
wm = 250.e-6
sigmaSub = 0.17
YoungModSub = 72.e9
phiCoat = 1.e-6
phiSub = 1.e-6
d = 6.83e-6
YoungModCoat = 72.e9
sigmaCoat = 0.17
R = data[:,0]*12500.e-6

analytic = np.sqrt((2*kB*T/((math.pi**2)*f))*((1-(sigmaSub**2))/(wm*YoungModSub))*(d/wm)*((phiCoat)/(YoungModSub*YoungModCoat*(1-sigmaCoat**2)*(1-sigmaSub**2)))*(YoungModCoat**2*(1+sigmaSub)**2*(1-2*sigmaSub)**2+YoungModSub**2*(1+sigmaCoat)**2*(1-2*sigmaCoat)))
analyticCoatingNoise = [analytic for row in range(len(data))]

fig = plt.gcf()
ax = plt.gca()

gridwidth=0.5
gridcolor=(0.8,0.8,0.8)

ax.plot(d/R, analyticCoatingNoise, marker='None', label='Approx. analytic', color='b', linestyle='dashed')
ax.plot(d/R, coatingNoise/np.sqrt(f), marker='D', label='Numerical', color='k')
#ax.set_yscale('log')
ax.set_xscale('log')
#ax.set_ylim([5.9e-19,6.9e-19])
ax.set_xlabel('$d/R$', fontsize=myAxisLabelSize)
ax.set_ylabel(r'$\sqrt{S_q} \left(\mathrm{m}/\sqrt{\mathrm{Hz}}\right)$', fontsize=myAxisLabelSize)
ax.tick_params(axis='x', labelsize=myTickLabelSize, pad=12, length=10)
ax.tick_params(which='minor', length=5)
ax.tick_params(axis='y', labelsize=myTickLabelSize, length=10)
ax.set_title('Fused silica coating noise', fontsize=myTitleSize, color='k', y=1.04)
ax.grid(b=True, which='major', color=gridcolor, linestyle='solid', linewidth=gridwidth)
ax.legend(loc='best', fontsize=myLegendLabelSize)

fig.tight_layout()
pdf = PdfPages('VaryMirrorNoise.pdf')
pdf.savefig()
pdf.close()



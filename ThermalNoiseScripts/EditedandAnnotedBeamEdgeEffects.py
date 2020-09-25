import numpy as np
import matplotlib
from matplotlib import pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import math

data = np.genfromtxt("VaryBeamEnergy_c08_AlGaAs.dat")

# Coating noise is on the third coloum
coatingNoise = data[:,2]
# Defined before Eq. 5 as r0 = w/sqrt(2)
# we multiply by e-6 because these are in micrometers
r_0 = data[:,0]*250.e-6/np.sqrt(2)
kB = 1.3806488e-23
# Temperature used and defined in the code
T = 300.
# Frequency
f = 100.
# Some papers use this def of r0.
wm = data[:,0]*250.e-6
# These are the values for the 
# silica substrate
sigmaSub = 0.17
YoungModSub = 72.e9
# Loss angles of the coating.
# Recall for a substrate with a single coating
# phi_FusedSilica = 1.e-6
# phi_Iso_Ta2O5 = 4.e-4
# phi_iso_AlGaAs = 2.5e-5
# phi_AlGaAs = 2.5 e-5
phiCoat = 2.5e-5
phiSub = 1.6e-6
d = 6.83e-6
# These needs to be changed for each coating
# The values for these are listed in Table 1
# of the paper.
YoungModCoat = 100.e9
sigmaCoat = 0.32
R = 12500.e-6

analytic = np.sqrt((2*kB*T/((math.pi**2)*f))*((1-(sigmaSub**2))/(wm*YoungModSub))*(d/wm)*((phiCoat)/(YoungModSub*YoungModCoat*(1-sigmaCoat**2)*(1-sigmaSub**2)))*(YoungModCoat**2*(1+sigmaSub)**2*(1-2*sigmaSub)**2+YoungModSub**2*(1+sigmaCoat)**2*(1-2*sigmaCoat)))


myAxisLabelSize=32
myTickLabelSize=24
myLegendLabelSize=10
myTitleSize=25

fig = plt.gcf()
ax = plt.gca()

gridwidth=0.5
gridcolor=(0.8,0.8,0.8)


# These first set of lines are Nick's original code.
ax.plot(d/r_0, analytic, marker='None', label='Approx. analytic', color='b', linestyle='dashed')
ax.plot(d/r_0, coatingNoise/np.sqrt(f), marker='None', label='Numerical', color='k')
ax.set_xlabel('$d/r_0$', fontsize=myAxisLabelSize)

# These
#ax.plot(d/r_0, analytic, marker='None', label='Approx. analytic', color='b', linestyle='dashed')
#ax.plot(d/r_0, coatingNoise/np.sqrt(f), marker='None', label='Numerical', color='k')
#ax.set_xlabel('$d/r_0$', fontsize=myAxisLabelSize)

ax.set_yscale('log')
ax.set_xscale('log')
# ax.set_ylim([6.9e-22, 5.9e-17])

ax.set_ylabel(r'$\sqrt{S_q} \left(\mathrm{m}/\sqrt{\mathrm{Hz}}\right)$', fontsize=myAxisLabelSize)
ax.tick_params(axis='x', labelsize=myTickLabelSize, pad=12, length=10)
ax.tick_params(which='minor', length=5)
ax.tick_params(axis='y', labelsize=myTickLabelSize, length=10)
ax.set_title('AlGaAs coating', fontsize=myTitleSize, color='k', y=1.04)
ax.grid(b=True, which='major', color=gridcolor, linestyle='solid', linewidth=gridwidth)
ax.legend(loc='upper left', shadow=True, fontsize=myLegendLabelSize, prop={'size': 12})

fig.tight_layout()
pdf = PdfPages('VaryBeamNoise_AlGaAs_theoretical.pdf')
pdf.savefig()
pdf.close()



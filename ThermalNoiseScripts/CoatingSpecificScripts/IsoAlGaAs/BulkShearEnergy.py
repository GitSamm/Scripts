import numpy as np
import matplotlib
from matplotlib import pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

myAxisLabelSize=32
myTickLabelSize=18
myLegendLabelSize=14
myTitleSize=25

data = np.genfromtxt("Energy.dat")

bulkEnergy = data[:,10]
shearEnergy = data[:,11]

BulkPhi = 2.5e-5
ShearPhi = 2.5e-5

BulkPhiDividedByShearPhi = BulkPhi/ShearPhi
BulkEnergyDividedByShearEnergy = bulkEnergy/shearEnergy

print(BulkEnergyDividedByShearEnergy)

fig = plt.gcf()
ax = plt.gca()

gridwidth=0.5
gridcolor=(0.8,0.8,0.8)


ax.plot(data[:,0], BulkEnergyDividedByShearEnergy, marker='o', label='Coating energy', color='r')

ax.set_xlim([0,12])
ax.set_ylim([1e-6,1e0])

ax.set_yscale('log')

ax.set_xlabel('$N$', fontsize=myAxisLabelSize)
ax.set_ylabel('$|E_{N+1} - E_{N}|/ E_{N+1}$ ', fontsize=myAxisLabelSize)

ax.tick_params(axis='x', labelsize=myTickLabelSize, pad=12, length=1)
ax.tick_params(which='minor', length=1)
ax.tick_params(axis='y', labelsize=myTickLabelSize, length=1)
ax.grid(b=True, which='major', color=gridcolor, linestyle='solid', linewidth=gridwidth)

ax.set_title('AlGaAs (effective isotropic)', fontsize=myTitleSize, color='k', y=1.04)
ax.legend(loc='lower left', fontsize=myLegendLabelSize)

fig.tight_layout()
pdf = PdfPages('BulkShearEnergy.pdf')
pdf.savefig()
pdf.close()

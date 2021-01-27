import h5py
import numpy as np
import matplotlib

matplotlib.use('agg')
from matplotlib import pyplot as plt


from matplotlib.backends.backend_pdf import PdfPages
import math


myAxisLabelSize=32
myTickLabelSize=18
myLegendLabelSize=14
myTitleSize=25

gridwidth=0.5
gridcolor=(0.8,0.8,0.8)

#Call in the file
file=h5py.File("Horizons.h5")
file.keys()

#Find the right directory for each black hole
file["AhA.dir"].keys()
file["AhB.dir"].keys()


coordA=file["AhA.dir"]["CoordCenterInertial.dat"]
coordB=file["AhB.dir"]["CoordCenterInertial.dat"]

plt.figure(figsize = [7,7])
plt.plot(coordA[:,1],coordA[:,2], label = 'm1, (0, 0, 0.95)' ) 
plt.plot(coordB[:,1],coordB[:,2], label = 'm2, (0, 0, 0.95)' )
plt.legend(loc='upper left')

# Set the xlimit and ylimit accordingly.
# Make each  
plt.title('Trajectory')
plt.xlim([-15,15])
plt.ylim([-15,15])
plt.grid(b=True, which='major', color=gridcolor, linestyle='solid', linewidth=gridwidth)

plt.savefig('Trajectories.png')

pdf = PdfPages('Trajectories.pdf')
pdf.savefig()
pdf.close()
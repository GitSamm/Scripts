#!/usr/bin/env python

# Use simulation time and total mass tp quickly find the real time in seconds.

from argparse import ArgumentParser, RawTextHelpFormatter
import argparse

p = ArgumentParser(usage=__doc__, formatter_class=RawTextHelpFormatter)
p.add_argument('--tMerger', type=float, required=True, help = "Approximate time of merger") 
p.add_argument('--totalmass', type=float, required=True, help = "Total Mass") 
opts = p.parse_args()


# The mass of the sun is 1.989 E 1030 kg
MassOfSun = 1.989E30
# BIG G = 6.673 x 10-11 N m2 kg-2

G = 6.673E-11
c = 299792458
cCubed = c*c*c

NormalizingFactor = G/cCubed

realTime = MassOfSun * NormalizingFactor * opts.tMerger * opts.totalmass

print(realTime)
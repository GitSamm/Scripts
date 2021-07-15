# Use this script to run paraview on ocean

#!/bin/bash -
#SBATCH -o paraview.stdout
#SBATCH -e paraview.stderr
#SBATCH --ntasks-per-node 20
#SBATCH -J paraview
#SBATCH --nodes 1
#SBATCH -p orca-1
#SBATCH -t 12:00:00
#SBATCH -D .

# Distributed under the MIT License.
# See LICENSE.txt for details.

# Set script path
PARAVIEW_SCRIPT=pvtest.py

# Set desired permissions for files created with this script
umask 0022

# Load modules
source /home/geoffrey/apps/spack/share/spack/setup-env.sh 

# There are three different paraview modules loaded. If this 
# one does not work for you, try anther. If none work, 
# conatact Geoffrey.

spack load paraview/5tgbeko

# Run paraview
echo "Starting pvbatch..."
date

mpirun -np 20 pvbatch ${PARAVIEW_SCRIPT} &> paraview.out

echo "Done."
date

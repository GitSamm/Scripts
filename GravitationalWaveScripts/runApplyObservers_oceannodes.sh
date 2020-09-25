#!/bin/bash -
#SBATCH -o spec.stdout
#SBATCH -e spec.stderr
#SBATCH --ntasks-per-node 20
#SBATCH -J GW
#SBATCH -n 20
#SBATCH -p orca-1
#SBATCH -t 1000:00:00 


umask 0022
. ./bin/this_machine.env || echo 'Not using env file.'
set -x
export PATH=$(pwd -P)/bin:$PATH

mpirun -np 20 ./bin/ApplyObservers -domaininput GrDomain.input -v -t psi,kappa -r 11,122 -d 4,4 DumpPsi4.input &> ApplyObservers.out
 


#!/bin/bash -
#SBATCH -o spec.stdout
#SBATCH -e spec.stderr
#SBATCH --ntasks-per-node 20
#SBATCH -J VortexTendex
#SBATCH -n 20
#SBATCH -p orca-1
#SBATCH -t 1000:00:00


umask 0022
. ./bin/this_machine.env || echo 'Not using env file.'
set -x
export PATH=$(pwd -P)/bin:$PATH

./bin/ApplyObservers -v -domaininput GrDomain.input -t VTWeylE,VTWeylB,Inertialg -d 3,3,3 -r 11,11,11 ApplyObservers.input

#comment out -domaininput GrDomain.input if you have the origonal Domain.input file. This flag will cause the job to crash.

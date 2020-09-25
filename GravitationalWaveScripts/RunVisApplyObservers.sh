#!/bin/bash -
#PBS -l nodes=1:ppn=12
#PBS -l walltime=100:0:00


#PBS -N ConvertPsi4
#PBS -o SpEC.stdout
#PBS -e SpEC.stderr
#PBS -q express
#PBS -d .
#PBS -W umask=022
#PBS -S /bin/bash
# This is for submitting a batch job on orca.
umask 0022
. this_machine.env || echo 'Not using env file.'
set -x
export PATH=$(pwd -P)/bin:$PATH

mpirun -np 12 ./ApplyObservers -v -NoDomainHistory -s 10 -ReadTimesFromH5File=./data/Vars_SphereC0.h5 VisGW.input &> ApplyObservers.out
 


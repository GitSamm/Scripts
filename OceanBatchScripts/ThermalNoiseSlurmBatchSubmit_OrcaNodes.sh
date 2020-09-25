#!/bin/bash -
#SBATCH -J TN_Cyl_Crystal             # Job Name
#SBATCH -o ElastostaticMirror.stdout  # Output file name
#SBATCH -e ElastostaticMirror.stderr  # Error file name
#SBATCH -n 284                        # Number of nodes
#SBATCH --ntasks-per-node 12          # number of MPI ranks per node
#SBATCH -p orca-0                     # Queue name
#SBATCH -t 36:0:00                    # Run time

#Machine-specific module information...
#edit to set up your bash environment on your cluster
#this section is machine dependent
#you can comment out this section if you don't use modules

umask 0022 #others have read permission to the results
module purge
cp /home/samuel/bin/dealii_modules_orca0.sh .
source ./dealii_modules_orca0.sh
dealii_load_modules

module list #print loaded modules

cp ../QuasistaticBrownianThermalNoise .
cp ../QuasistaticBrownianThermalNoise.cpp .


#mpirun -np 240 QuasistaticBrownianThermalNoise --configuration=./config.yaml --configuration_multloss=./config_multloss.yaml &> QuasistaticBrownianThermalNoise.out


mpirun -np 284 QuasistaticBrownianThermalNoise --configuration=./config.yaml --configuration_multloss=./config_multloss.yaml &> QuasistaticBrownianThermalNoise.out

#mpirun -np 240 QuasistaticBrownianThermalNoise -ksp_monitor -snes_monitor -options_table &> QuasistaticBrownianThermalNoise.out


#!/bin/bash -

# I really should write a python file that creates a dat list with certain radii. Then I can parse through that list to make the directories. It would be 
# easier than trying to make those directories with these bash commands.

F0=.001
runtests=False
numberofNodes=240
numberofCycles=11
coatingMaterial=Iso_FusedSilica

# Since there are two different queues that we can run this script on, we pass the bash script that submits a job to the cluster to a variable.

phi11=2.5e-5
phi12=2.5e-5
phi44=2.5e-5

script=ThermalNoiseSlurmBatchSubmit_OceanNodes.sh


for d in */ ; do

    # Copy the needed files
    # All of these files are needed to run the jobs, change path names as neccesary. 

     cp ../QuasistaticBrownianThermalNoise ./$d
     cp ../*.sh ./$d
     cp ../../QuasistaticBrownianThermalNoise.cpp ./$d
     cp ../../config.yaml ./$d
     cp ../../config_multloss.yaml ./$d
          
     cd ./$d #Change into the current directory.
     
     # Se the correct script to edit.
     path=$PWD
     bashscript=$path/$script

     result=${PWD##*/} # Get the name of only the directory, and not the absolute path.
     result2=${result:7:11} # Get the size of the radius. This command assumes the name of each of the directories is called c10_r0_####, so it will take the assign the value of the 7th character through the 11th character to the variable.

     sed -i "s/F0: 0.001/F0: $F0/g"                                              config.yaml #Change the value of the radius.
     sed -i "s/Radius: 176.77669534/Radius: $result2.77669534/g"                 config.yaml #Change the value of the radius.
     sed -i "s/CoatingMaterial: Iso_AlGaAs/CoatingMaterial: $coatingMaterial/g"  config.yaml #Change the value of the radius.
     sed -i "s/RunTests: True/RunTests: $runtests/g"                             config.yaml #Change the number of cycles.
     sed -i "s/Cycles: 1/Cycles: $numberofCycles/g"                              config.yaml #Change the number of cycles.
     #sed -i "s/Phi11: 2.5e-5/Phi11: $phi11/g"  config_multloss.yaml
     #sed -i "s/Phi12: 2.5e-5/Phi12: $phi12/g"  config_multloss.yaml
     #sed -i "s/Phi44: 2.5e-5/Phi44: $phi44/g"  config_multloss.yaml
     sed -i "s/#SBATCH -J TN_Cyl_Crystal/#SBATCH -J TN_Crystal_$result2/g"  $bashscript #Rename the job on the cluster
     sed -i "s/#SBATCH -n 240/#SBATCH -n $numberofNodes/g" $bashscript
     sed -i "s/mpirun -np 240/mpirun -np $numberofNodes/g" $bashscript

     
     sbatch $bashscript # ThermalNoiseSlurmBatchSubmit_v2.sh # Submit the job to the cluster
     cd ../

    done

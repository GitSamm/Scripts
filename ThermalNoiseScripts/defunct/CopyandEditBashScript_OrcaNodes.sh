# I really should write a python file that creates a dat list with certain radii. Then I can parse through that list to make the directories. 
# Then this bash script can just run that python script. Who knows. Maybe it wouldn't be easier

# This script needs to be ran in a build/Data/ directory.
# It assumes that ThermalNoiseSlurmBatchSubmit_OrcaNodes.sh lives inside of ./Data/


for d in */ ; do

    # Copy the needed files
    # Right now the paths are hardcoded, but in the future, we would like to use the abosulute path so that we can run this from anywhere.

     cp ../QuasistaticBrownianThermalNoise ./$d
     cp ./ThermalNoiseSlurmBatchSubmit_OrcaNodes.sh ./$d
     cp ../../QuasistaticBrownianThermalNoise.cpp ./$d
     cp ../../config.yaml ./$d
     cp ../../config_multloss.yaml ./$d
          
     cd ./$d #Change into the current directory.
     result=${PWD##*/} # Get the name of only the directory, and not the absolute path.
     result2=${result:7:11} # Get the size of the radius. This command assumes the name of each of the directories is called c10_r0_####, so it will take the assign the value of the 7th character through the 11th character to the variable.

     node=20 # Ranges from 0-47 currently. Try not to use more than 20 at a time

     sed -i "s/Radius: 176.77669534/Radius: $result2.77669534/g"       config.yaml #Change the value of the radius.
     sed -i "s/CoatingMaterial: Iso_AlGaAs/CoatingMaterial: AlGaAs/g"  config.yaml #Change the value of the radius.
     sed -i "s/Cycles: 1/Cycles: 13/g" config.yaml #Change the number of cycles
     sed -i "s/RunTests: True/RunTests: False/g" config.yaml #Change whether the tests are ran.
     sed -i "s/UseMultipleLossAngles: True/UseMultipleLossAngles: True/g"  config_multloss.yaml # Choose whether or not to use multiple loss angles
#     sed -i "s/Bulk:  2.5e-5/Bulk:  2.5e-5/g"  config_multloss.yaml # Bulk loss angle for Iso_AlGaAs
#     sed -i "s/Shear: 2.5e-5/Shear: 2.5e-5/g"  config_multloss.yaml # Shear loss angle for Iso_AlGaAs
     sed -i "s/Phi11: 2.5e-5/Phi11: 2.5e-5/g"  config_multloss.yaml # Coating needs to be set to AlGaAs for this to work
     sed -i "s/Phi12: 2.5e-5/Phi12: 2.5e-5/g"  config_multloss.yaml # Coating needs to be set to AlGaAs for this to work
     sed -i "s/Phi44: 2.5e-5/Phi44: 2.5e-5/g"  config_multloss.yaml # Coating needs to be set to AlGaAs for this to work
     sed -i "s/#SBATCH -J TN_Cyl_Crystal/#SBATCH -J TN_Crystal_$result2/g" ThermalNoiseSlurmBatchSubmit_OrcaNodes.sh #Rename the job on the cluster
     sed -i "s/#SBATCH --nodes 20/#SBATCH --nodes $node/g" ThermalNoiseSlurmBatchSubmit_OrcaNodes.sh #Change the number of nodes
     sed -i "s/mpirun -np 20/mpirun -np $node/g" ThermalNoiseSlurmBatchSubmit_OrcaNodes.sh #Change the number of nodes
     
#     sbatch ThermalNoiseSlurmBatchSubmit_OrcaNodes.sh # Submit the job to the cluster
     cd ../

    done



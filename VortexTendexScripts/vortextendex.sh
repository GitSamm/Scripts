mkdir vortextendex
cd vortextendex

ln -s ../Run/*input . 
ln -s ../Run/Hist*txt .

ln -s ../Run/Streamlines/*h5 . 
ln -s ../Run/ApparentHorizons/Ah?Coefs.dat .
ln -s ../Run/ApparentHorizons .
ln -s ../Run/OrbitDiagnostics.h5 .

ExtractFromH5 OrbitDiagnostics.h5
mv extracted-OrbitDiagnostics/Orbit* .

# If you have a different copy of SpEC link it to that bin. 
# This generic ln will link it to the copy of SpEC that created the initial data.

ln -s ../bin .
# /home/samuel/scripts/VortexTendexScripts/*
cp /home/samuel/VortexTendexFiles/ApplyObserversNew.input .
cp /home/samuel/VortexTendexFiles/setcenters.sh . 
cp /home/samuel/VortexTendexFiles/makeapplyobservers.py .
cp /home/samuel/VortexTendexFiles/run_ApplyObservers_orca.sh .
cp /home/samuel/VortexTendexFiles/run_ApplyObservers_ocean.sh .

# By default, will only change Vortex lines, Tendex Lines, and the centers of the black holes.
# The center is the same for each throughout each level.

# Change the initializer. Change the initialzer that you want to one and the others to zero.                                                                         
# The default initialzer in makeapplyobservers.py is seeding the lines from the horizon.                                                                             

sed -i 's/ApparentHorizon=0/ApparentHorizon=1/g'                          makeapplyobservers.py
sed -i 's/OrbitalApparentHorizon = 0/OrbitalApparentHorizon = 0/g'        makeapplyobservers.py
sed -i 's/SpecifyPointAndEigenvector = 0/SpecifyPointAndEigenvector=0/g'  makeapplyobservers.py
sed -i 's/DriftVelocity = 0/DriftVelocity = 0/g'                          makeapplyobservers.py
sed -i 's/DotProduct = 0/DotProduct = 0/g'                                makeapplyobservers.py


# These are general options

sed -i 's/VortexA=0/VortexA=0/g' makeapplyobservers.py
sed -i 's/VortexB=0/VortexB=0/g' makeapplyobservers.py
sed -i 's/VortexC=0/VortexC=0/g' makeapplyobservers.py

sed -i 's/TendexA=0/TendexA=0/g' makeapplyobservers.py
sed -i 's/TendexB=0/TendexB=0/g' makeapplyobservers.py
sed -i 's/TendexC=0/TendexC=0/g' makeapplyobservers.py

# Apparent Horizon Initializer Options

sed -i 's/CenterA = "()"/CenterA = "()"/g'  makeapplyobservers.py
sed -i 's/CenterB = "()"/CenterB = "()"/g'  makeapplyobservers.py
sed -i 's/CenterC = "()"/CenterC = "()"/g'  makeapplyobservers.py

# SpecifyPointandEigenVector Options

sed -i 's/TendexSpecEig = 0/TendexSpecEig = 0/g' makeapplyobservers.py
sed -i 's/VortexSpecEig = 0/VortexSpecEig = 0/g' makeapplyobservers.py

sed -i 's/Eigenvector = "1"/Eigenvector = "1"/g' makeapplyobservers.py
sed -i 's/SPE_StartPoints = " (-3,-3,-3),(-3,-3,-2),(-3,-3,-1)"/SPE_StartPoints = "(-3,-3,-3),(-3,-3,-2),(-3,-3,-1)"/g' makeapplyobservers.py


# DotProductInitializer Options

sed -i 's/TendexDotEig = 0/TendexDotEig = 0/g' makeapplyobservers.py
sed -i 's/VortexDotEig = 0/VortexDotEig = 0/g' makeapplyobservers.py

sed -i 's/Dot_StartPoints = " (-3,-3,-3),(-3,-3,-2),(-3,-3,-1)"/Dot_StartPoints = "(-3,-3,-3),(-3,-3,-2),(-3,-3,-1)"/g' makeapplyobservers.py
sed -i 's/NormalizedVector = "(1,0,0)"/NormalizedVector = "(1,0,0)"/g' makeapplyobservers.py


# Change the name of that appears in the queue.

sed -i 's/VortexTendex/VortexTendex/g' run_ApplyObservers_orca.sh
sed -i 's/VortexTendex/VortexTendex/g' run_ApplyObservers_ocean.sh


# Run this command to create   Applyobserver.input.    

python makeapplyobservers.py

# Uncomment out the line below in order to run the job from this script.


#sbatch run_ApplyObservers_orca.sh
#sbatch run_ApplyObservers_ocean.sh


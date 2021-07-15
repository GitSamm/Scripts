

################################################################################################                                                                                                  ################################################################################################                                                                              

# This file makes the horizon, vortex, and tendex vtk files that can be used in paraview inside of a created directry, Streamlines_Horizons.

################################################################################################################################################################################################################################################################################################################################################################################################

mkdir Streamlines_Horizons
cd    Streamlines_Horizons

cp ../Run/ApparentHorizons/HorizonsDump.h5 ./

ConvertH5SurfaceToVtk HorizonsDump.h5
rm                    HorizonsDump.h5

cd ../Vis/Streamlines/
ConvertStreamlinesToVtk -n Tendex_AA Tendex*.dat
ConvertStreamlinesToVtk -n Vortex_AA Vortex*.dat
cp *_AA* ../../Streamlines_Horizons/

cd ../../Streamlines_Horizons/
pwd
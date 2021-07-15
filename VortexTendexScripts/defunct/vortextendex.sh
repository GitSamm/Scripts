mkdir Vis
cd Vis

ln -s ../Run/*input . 
ln -s ../Run/Hist*txt .

ln -s ../Run/Streamlines/*h5 . 
ln -s ../Run/ApparentHorizons/Ah?Coefs.dat .
ln -s ../Run/ApparentHorizons .

ln -s ../bin .

cp /home/haroonkhan/haroonkhan/VortexTendex/requiredFiles/visfiles/ApplyObserversNew.input  .
cp /home/haroonkhan/haroonkhan/VortexTendex/requiredFiles/visfiles/run_ApplyObservers.sh .
cp /home/haroonkhan/haroonkhan/VortexTendex/requiredFiles/visfiles/setcenters.sh .
cp /home/haroonkhan/haroonkhan/VortexTendex/requiredFiles/visfiles/makeapplyobservers.py .


mkdir gws
cd gws


ln -s ../Run/*input . 
ln -s ../Run/Hist*txt .
ln -s ../Run/ApparentHorizons/Ah?Coefs.dat .
ln -s ../Run/ApparentHorizons .


ln -s ../bin/ .

cp /home/samuel/bin/GravitationalWaveScripts/DumpPsi4.input .
cp /home/samuel/bin/GravitationalWaveScripts/RunApplyObservers.sh .


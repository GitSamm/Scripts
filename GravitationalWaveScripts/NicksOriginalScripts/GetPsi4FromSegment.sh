#!/bin/bash
for var in "$@"
do
lev=$(basename $var)
echo $lev
#mkdir $lev
pushd $lev
cp ../DumpPsi4.input .
cp ../RunApplyObservers.sh .
cp ../SubmitVis.sh .
ln -s ../$var/Run/{Domain.input,SpatialCoordMap.input,RefinementOptionHistory.input} .
ln -s ../$var/bin/this_machine.env .
ln -s ../$var/bin/ApplyObservers .
qsub SubmitVis.sh
popd
done

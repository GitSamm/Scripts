#!/bin/bash
for var in "$@"
do
work=`pwd`
lev=$var
cd $lev
mkdir Vis
cd Vis
ln -s ../Domain.input .
ln -s ../SpatialCoordMap.input .
ln -s ../Hist*txt .
ln -s ../RefinementOptionHistory.input .
cp $work/VisGW.input .
cp $work/RunVisApplyObservers.sh .
cp $work/SubmitConvert.sh .
cp ../this_machine.env .
. ./this_machine.env
ln -s ../ApplyObservers .

mkdir data
cd data
ln -s ../../GWVisData/*h5 .

#Could replace Domain.input with a higher resolution grid, but try the same domain for now
ln -s ../Domain.input .
ln -s ../SpatialCoordMap.input .
ln -s ../Hist*txt .
ln -s ../RefinementOptionHistory.input .

cd ..
qsub SubmitConvert.sh
cd $work
done
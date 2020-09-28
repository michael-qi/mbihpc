#!/bin/bash
#PBS -l walltime=24:00:00
#PBS -l select=1:mem=400mb:ncpus=1:ngpus=1
#PBS -N JobArray
#PBS -J 1-100:2
#PBS -e log
#PBS -m ae
#PBS -o log
#PBS -P hpc_common


hostname
sleep 10
outfile=~/jobscript/arrout/`hostname`-$PBS_ARRAY_INDEX.txt
hostname >> $outfile
echo -e "arrayindex\t" $PBS_ARRAY_INDEX >> $outfile

./yourapp $PBS_ARRAY_INDEX

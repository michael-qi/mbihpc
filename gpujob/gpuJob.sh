#!/bin/bash
#PBS -l walltime=24:00:00
#PBS -l select=1:ncpus=1:ngpus=1:mem=2gb
#PBS -N hello_Word
#PBS -e log
#PBS -m ae
#PBS -o log
#PBS -P hpc_common


module load nvidia/nvhpc/20.7

hostname
sleep 10
hostname > `hostname`.txt
echo $TMPDIR >> `hostname`.txt


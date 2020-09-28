#!/bin/bash
#PBS -l walltime=24:00:00
#PBS -l select=1:mem=400mb:ncpus=4:ngpus=0:cpu_arch=amd
#PBS -N hello_Word
#PBS -e log
#PBS -M qi20@nus.edu.sg
#PBS -m ae
#PBS -o log
#PBS -q testing
#PBS -P hpc_common

hostname
hostname > `hostname`.txt
echo $TMPDIR >> `hostname`.txt

#!/bin/bash
#PBS -l walltime=1:00:00
#PBS -l select=1:mem=400mb:ncpus=4:ngpus=0
#PBS -N hello_Word
#PBS -e log
#PBS -o log
#PBS -q testing
#PBS -P hpc_common

cd ~/workproject
hostname
sleep 10
hostname > `hostname`.txt
echo $TMPDIR >> `hostname`.txt

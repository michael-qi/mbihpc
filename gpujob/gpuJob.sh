#!/bin/bash
#PBS -l walltime=1:00:00
#PBS -l select=1:mem=400mb:ncpus=4:ngpus=1
#PBS -N GPU_JOB
#PBS -e log
#PBS -o log
#PBS -q testing
#PBS -P hpc_common

cd ~/mpihpc/gpujob
hostname
nvidia-smi
module purge
module load nvidia/nvhpc/20.7
hostname > `hostname`.txt
./gpu_burngcc 30 >> `hostname`.txt

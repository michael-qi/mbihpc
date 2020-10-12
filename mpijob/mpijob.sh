#!/bin/bash
#PBS -l walltime=24:00:00
#PBS -l select=1:mem=24000mb:ncpus=36:ngpus=0:mpiprocs=36:cpu_arch=amd
#PBS -N mpi_job
#PBS -M qi20@nus.edu.sg
#PBS -m abe
#PBS -e log
#PBS -o log
#PBS -P hpc_common


cd ~/mbihpc/mpijob
module load intel
mpirun -np 36 ./aproc

#!/bin/bash
#PBS -l walltime=24:00:00
#PBS -l select=1:mem=24000mb:ncpus=4:ngpus=2
#PBS -N GPU_jupyter
#PBS -e log
#PBS -o log
#PBS -P hpc_common


cd ~/jupyterjob
module load anaconda/3

XDG_RUNTIME_DIR=""
ipnport=$(shuf -i8000-9999 -n1)
ipnip=$(hostname -i)
outputfile=`hostname`.$PBS_JOBID

echo -e "\n"   									>> $outputfile
echo    "  Paste ssh command in a terminal on local host (i.e., laptop)"	>> $outputfile
echo    "  ------------------------------------------------------------"	>> $outputfile
echo -e "  ssh -N -L $ipnport:$ipnip:$ipnport $USER@milo.mbi.nus.edu.sg\n"	>> $outputfile
echo    "  Open this address in a browser on local host; see token below"	>> $outputfile
echo    "  ------------------------------------------------------------"	>> $outputfile
echo -e "  localhost:$ipnport                                      \n\n"	>> $outputfile

jupyter-notebook --no-browser --port=$ipnport --ip=$ipnip --NotebookApp.token='' --NotebookApp.password=''

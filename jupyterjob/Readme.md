The job script will submit a jupyter notebook on the compute node. After submit this job with "qsub", to connect the jupyter server please follow this steps:

1. Run 'qstat' to check the job is running normally.

2. In the working directory find out the job's output. Print out this file on the screen.

3. Copy/paste this in your another local terminal to setup the "ssh tunnel" with remote
ssh -N -L 8193:10.214..:8193 yourID@milo.mbi.nus.edu.sg

4. Then open a browser on your local machine to the following address
localhost:8193 (prefix w/ https:// if using password)


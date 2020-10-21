test 1

```bash
 mpirun -n 12 ior -t 1m -b 16m -s 16
[milo:119818] mca: base: component_find: unable to open /cm/shared/apps/openmpi/gcc/64/1.10.7/lib64/openmpi/mca_ess_tm: libpbs.so.0: cannot open shared object file: No such file or directory (ignored)
[milo:119818] mca: base: component_find: unable to open /cm/shared/apps/openmpi/gcc/64/1.10.7/lib64/openmpi/mca_plm_tm: libpbs.so.0: cannot open shared object file: No such file or directory (ignored)
[milo:119818] mca: base: component_find: unable to open /cm/shared/apps/openmpi/gcc/64/1.10.7/lib64/openmpi/mca_ras_tm: libpbs.so.0: cannot open shared object file: No such file or directory (ignored)
IOR-3.4.0+dev: MPI Coordinated Test of Parallel I/O
Began               : Fri Oct  2 13:10:15 2020
Command line        : ior -t 1m -b 16m -s 16
Machine             : Linux milo
TestID              : 0
StartTime           : Fri Oct  2 13:10:15 2020
Path                : testFile
FS                  : 1537.5 TiB   Used FS: 67.5%   Inodes: 376.9 Mi   Used Inodes: 47.5%

Options: 
api                 : POSIX
apiVersion          : 
test filename       : testFile
access              : single-shared-file
type                : independent
segments            : 16
ordering in a file  : sequential
ordering inter file : no tasks offsets
nodes               : 1
tasks               : 12
clients per node    : 12
repetitions         : 1
xfersize            : 1 MiB
blocksize           : 16 MiB
aggregate filesize  : 3 GiB

Results: 

access    bw(MiB/s)  IOPS       Latency(s)  block(KiB) xfer(KiB)  open(s)    wr/rd(s)   close(s)   total(s)   iter
------    ---------  ----       ----------  ---------- ---------  --------   --------   --------   --------   ----
write     29629      30256      0.004382    16384      1024.00    0.002544   0.101533   0.031020   0.103681   0   
read      3190.35    3190.44    0.056129    16384      1024.00    0.000193   0.962876   0.558622   0.962904   0   

Summary of all tests:
Operation   Max(MiB)   Min(MiB)  Mean(MiB)     StdDev   Max(OPs)   Min(OPs)  Mean(OPs)     StdDev    Mean(s) Stonewall(s) Stonewall(MiB) Test# #Tasks tPN reps fPP reord reordoff reordrand seed segcnt   blksiz    xsize aggs(MiB)   API RefNum
write       29629.36   29629.36   29629.36       0.00   29629.36   29629.36   29629.36       0.00    0.10368         NA            NA     0     12  12    1   0     0        1         0    0     16 16777216  1048576    3072.0 POSIX      0
read         3190.35    3190.35    3190.35       0.00    3190.35    3190.35    3190.35       0.00    0.96290         NA            NA     0     12  12    1   0     0        1         0    0     16 16777216  1048576    3072.0 POSIX      0
Finished            : Fri Oct  2 13:10:16 2020
```

# how to add a user
should login as amadmin on beehoon2. Before run any "amgr" command, the first step is to login "amgr login".

```bash
root# ssh amadmin
amadmin$ amgr login
```
1. create the user
```bash
#add a user
amgr add user -n zgqi -A end_period -c beehoon2-pbs.mbi.nus.edu.sg -r user -h hpc_grp -a 1

```
2. add the user into a cluster
```bash
amgr update user -n zgqi -c + beehoon2-pbs.mbi.nus.edu.sg
```

3. add the user into a project
```bash
amgr update project -n hpc_common -u + zgqi
```

# how to add a group
0. configure of amger, admin and roles
```bash
amgr add cluster -n beehoon2-pbs.mbi.nus.edu.sg
amgr add period -n my2024 -S 2020-01-01 -E 2024-12-31
amgr add serviceunit -n cpu_hrs -d "CPU Core Hours"
amgr add serviceunit -n gpu_hrs -d "GPU Core Hours"
amgr add user -n amteller -A begin_period -c beehoon2-pbs -r teller
amgr add user -n pbsadmin -A begin_period -c beehoon2-pbs -r investor
```
1. create a group
```bash
amgr add group -n hpc_grp -I pbsadmin -M pbsadmin -a 1
```
2. create a project
```bash
amgr add project -n hpc_common -A end_period -S '2020-09-01' -E '2024-12-31' -c beehoon2-pbs.mbi.nus.edu.sg -u zgqi -u aldavis -h hpc_grp

```
3. deposit money into the group (user: pbsadmin)
Note: in this step, should login as pbsadmin. Other steps work with amadmin user.
```base
amgr deposit group -n hpc_grp -s cpu_hrs 100000000 -C "Unlimited cpu_hrs Grant"
amgr deposit group -n hpc_grp -s gpu_hrs 100000000 -C "Unlimited gpu_hrs Grant"
```
4. update project to a group

5. attach money to the project (user: pbsadmin)
```bash
amgr deposit project -n hpc_common -s gpu_hrs 100000000 -p my2024 -h hpc_grp -C "Unlimited gpu_hrs Project Grant"
amgr deposit project -n hpc_common -s cpu_hrs 100000000 -p my2024 -h hpc_grp -C "Unlimited cpu_hrs Project Grant"
```

# deposit directly to a user
If the deposit directly goes to the user, then the user can submit jobs without the parameter "-P projectName".
```bash
amgr deposit user -n zgqi -s cpu_hrs 100 -p my2024 -h hpc_grp -C "test gpu_hrs Project Grant"
amgr deposit user -n zgqi -s gpu_hrs 200 -p my2024 -h hpc_grp -C "test gpu_hrs Project Grant"
```


# how to delete a project
```bash
# remove all the user for the project
amger update project -n project_name -u - username
# if there have CPU or GPU hours inside the porject, need to move them out firstly
# remove the project
amger rm project -n project_name
```


#!/bin/env /opt/anaconda3/bin/python3

#####################################################
# To collect the information about the users' usage 
# of the cluster.
# When PBSpro running, it will log all the information
# of each job in its accounting folder. The job script
# will parse these information and calculate the daily
# usage of each user.
# Author: Zhiguo Qi
# Date: 2020-10-20
#####################################################
import sys
import re
from pprint import pprint

# parse the log file and return the date about the job
def getTime(dtime):
    tmp = re.split(r"\s+",dtime)[0]
    tmp2 = re.split(r"\/",tmp)
    return "{}-{}-{}".format(tmp2[2],tmp2[0],tmp2[1])

# get the job state, the job state is instead by one
# Capital work.
def getState(state):
    pass

# get the job No. And remove other information, only 
# kept the number part.
def getJobNo(job):
    return re.split(r"\.",job)[0]

# get the resource usage of the job, and return a dictionary
# 
def getRes(resource):
    tmp = re.split(r"\s+",resource)
    iterNo = 0
    bunchget = False
    user = ''
    cpu_hrs = 0.0
    gpu_hrs = 0.0
    project = ""
    queue = ""
    host = ""
    mem = ""
    for item in tmp:
        if bunchget:
            if iterNo > 3:
                iterNo = 0
                bunchget = False
                continue
            else:
                if iterNo == 1:
                    cpu_hrs = float(item[:-1])
                if iterNo == 3:
                    gpu_hrs = float(item[:-2])
                iterNo += 1
                continue
        if "user" in item:
            user = re.split(r"=",item)[-1]
        if "project" in item:
            project = re.split(r"=",item)[-1]
        if "queue" in item:
            queue = re.split(r"=",item)[-1]
        if "exec_host" in item:
            host = re.split(r"=",item)[-1]
        if "resources_used.am_job_amount" in item:
            bunchget = True
            iterNo += 1
        if "resources_used.mem" in item:
            mem = re.split(r"=",item)[-1]
    #print("{} - {} - {} - {} - {} - {} - {}".format(user, project, queue, host, cpu_hrs, gpu_hrs, mem))
    return {
        "user"  :   user,
        "project": project,
        "queue": queue,
        "host": host,
        "cpu_hrs": cpu_hrs,
        "gpu_hrs": gpu_hrs,
        "mem"   : mem
    }

# this function is generating the resources comsumption of each user
def getSummary(rDicts):
    cpus = 0.0
    gpus = 0.0
    for key in rDicts.keys():
        for item in rDicts[key]:
            cpus += item["cpu_hrs"]
            gpus += item['gpu_hrs']
        print("{0:s} used {1:6.2f} CPU-Hours and {2:6.2f} GPU-Hours".format(key, cpus,gpus))
        cpus = 0.
        gpus = 0.

# here print the result on the screen.
def outputJobs(rDicts):
    for key in rDicts.keys():
        for item in rDicts[key]:
            print("{},{},{},{},{}".format(item['jobid'],item['user'],item['cpu_hrs'],item['gpu_hrs'],item['date']))


# print(sys.argv[1])
# filename is the account log file
filename = sys.argv[1]

# initial the resourse usage data dictionary
resDicts = {}

# read the log file
with open(filename,"r") as fp:
    Lines = fp.readlines() # read all the lines at once, Note: maybe the file could be closed here.
    for line in Lines: # parse the log file line by line
        tmp = re.split(r";",line)
        if len(tmp) == 4:
            if tmp[1] == "E":
                jobNo = getJobNo(tmp[2])
                tmp2 = getRes(tmp[3])
                date = getTime(tmp[0])
                tmp2["jobid"] = jobNo
                tmp2['date'] = date
                if tmp2['user'] in resDicts.keys():
                    resDicts[tmp2['user']].append(tmp2.copy())
                else:
                    resDicts[tmp2['user']] = [tmp2.copy()]
# pprint(resDicts)
# getSummary(resDicts)
outputJobs(resDicts)
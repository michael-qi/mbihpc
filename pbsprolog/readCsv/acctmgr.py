#!/bin/env /opt/anaconda3/bin/python3

import sys
import re
from pprint import pprint

def getTime(dtime):
    tmp = re.split(r"\s+",dtime)[0]
    tmp2 = re.split(r"\/",tmp)
    return "{}-{}-{}".format(tmp2[2],tmp2[0],tmp2[1])

def getState(state):
    pass

def getJobNo(job):
    return re.split(r"\.",job)[0]

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

def outputJobs(rDicts):
    for key in rDicts.keys():
        for item in rDicts[key]:
            print("{},{},{},{},{}".format(item['jobid'],item['user'],item['cpu_hrs'],item['gpu_hrs'],item['date']))

print(sys.argv[1])
filename = sys.argv[1]

resDicts = {}

with open(filename,"r") as fp:
    Lines = fp.readlines()
    for line in Lines:
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
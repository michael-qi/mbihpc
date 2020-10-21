#!/bin/env python3

import pandas as pd
import csv
import sys
import re

def getJobNo(jobno):
    if '[' in jobno:
        tmp = re.split(r'\.', jobno)[0][:-1]
        tmp2 = re.split(r'\[', tmp)
        no = tmp2[0]
        suno = tmp2[1]
        return "{}_{}".format(no,suno)
    else:
        no = re.split(r'\.', jobno)[0]
        return "{}".format(no)


userCsv = pd.read_csv("202010.csv",sep=',', delimiter=None, header='infer')


UserDict = {}
userAccount = {'cpu_hrs':0.0, 'gpu_hrs':0.0, 'user':'', 'date':''}




for index, row in userCsv.iterrows():
    jobid = getJobNo(row['transaction_id'])
    if jobid not in UserDict.keys():
        UserDict[jobid] = userAccount.copy()
        UserDict[jobid]['date'] = row['transaction_date']
        UserDict[jobid]['user'] = row['transaction_user']
        UserDict[jobid][row['serviceunit']] += row['amount'] if row['transaction_type'] == 'acquired' else -row['amount']
    else:
        UserDict[jobid][row['serviceunit']] += row['amount'] if row['transaction_type'] == 'acquired' else -row['amount']
    #if row['transaction_type'] == 'released':
    #    UserDict[jobid]['date'] = row['transaction_date']
    #    UserDict[jobid]['user'] = row['transaction_user']


for key in UserDict.keys():
    # print("{}'s job {} used CPU-Hours is {} and GPU-Hours is {} at {}".format(UserDict[key]['user'], key, UserDict[key]['cpu_hrs'], UserDict[key]['gpu_hrs'], UserDict[key]['date']))
    print("{},{},{},{},{}".format(UserDict[key]['user'], key, UserDict[key]['cpu_hrs'], UserDict[key]['gpu_hrs'], UserDict[key]['date']))

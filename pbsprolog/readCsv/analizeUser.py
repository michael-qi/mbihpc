#!/bin/env python3

import pandas as pd
import csv
import sys
import subprocess


userCsv = pd.read_csv("Sep_2020_report.csv",sep=',', delimiter=None, header='infer')


UserDict = {}
userAccount = {'cpu_hrs':0.0, 'gpu_hrs':0.0}



for index, row in userCsv.iterrows():
    user = row['transaction_user']
    if user not in UserDict.keys():
        UserDict[user] = userAccount.copy()
        UserDict[user][row['serviceunit']] += row['amount'] if row['transaction_type'] == 'acquired' else -row['amount']
    else:
        UserDict[user][row['serviceunit']] += row['amount'] if row['transaction_type'] == 'acquired' else -row['amount']


for key in UserDict.keys():
    print("{} used CPU-Hours is {} and GPU-Hours is {}".format(key, UserDict[key]['cpu_hrs'], UserDict[key]['gpu_hrs']))

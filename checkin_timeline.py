 #-*- coding: utf-8 -*-
"""checkin_timeline"""

import string
import csv
import re
import glob
import time

READ_PATH = r'result/weblog_*_preprocessed.csv'
SAVE_PATH = r'result/plaza_time_line.csv'

def time_trans(string):
    return time.strftime('%Y-%m-%d %H', time.localtime(float(string)))

def checkin_timeline(name):
    result = {}
    n = 0
    reader = csv.reader(open(name, 'rb'))
    for line in reader:
        n += 1
        if n % 100000 == 0:
            print n
        if line[0] != '' and line[1] != 'time':
            cmac = str(line[0])
            ts = float(line[1])
            if cmac not in result.keys():
                result[cmac] = ts
            
    login = {}
    for cmac in result:
        login_time = time_trans(result[cmac])
        if login_time not in login.keys():
            login[login_time] = 1
        else:
            login[login_time] += 1
        
    with open(SAVE_PATH, 'ab') as f:
        writer = csv.writer(f)
        for login_time in login:
            writer.writerow([login_time, login[login_time]])
        f.close()        

if __name__ == '__main__':
    print 'starting...'
    t_start = time.time()
    textList = glob.glob(READ_PATH)
    for each_file in textList:
        print each_file
        checkin_timeline(each_file)
    t_end = time.time()
    print 'cost %f sec' % (t_end - t_start)
    print 'ending...'

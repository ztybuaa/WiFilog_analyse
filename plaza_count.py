 #-*- coding: utf-8 -*-
"""plaza_count"""

import string
import csv
import re
import glob
import time

READ_PATH = r'result/weblog_*_preprocessed_count.csv'
SAVE_PATH = r'result/plaza_count.csv'

def plaza_count(name):
    count = {}
    during = {}
    num_cmac = {}
    reader = csv.reader(open(name, 'rb'))
    for line in reader:
        plaza = str(line[1])
        if plaza != 'plaza_id' and plaza != '' and str(line[0]) != '':
            if plaza not in count.keys():
                count[plaza] = []
                during[plaza] = []
                num_cmac[plaza] = 1
                count[plaza].append(int(line[2]))
                during[plaza].append(int(line[5]))
            else:
                count[plaza].append(int(line[2]))
                during[plaza].append(int(line[5]))
                num_cmac[plaza] += 1

    average_count = {}
    average_during = {}
    for each_plaza in count:
        total_count = 0
        for each in count[each_plaza]:
            total_count += int(each)
        average_count[each_plaza] = total_count  * 1.0 / len(count[each_plaza])
            
    for each_plaza in during:
        total_during = 0
        for each in during[each_plaza]:
            total_during += int(each)
        average_during[each_plaza] = total_during * 1.0 / len(during[each_plaza]) 
         
    with open(SAVE_PATH, 'ab') as f:
        writer = csv.writer(f)
        writer.writerow(['date', str(name).replace('portal.ffan.com-access_log_','').replace('_result.csv_plaza_count.csv','')])
        for plaza in average_count:
            line = []
            line.append(plaza)
            line.append(average_count[plaza])
            line.append(average_during[plaza])
            line.append(num_cmac[plaza])
            writer.writerow(line)
        f.close()        

if __name__ == '__main__':
    print 'starting...'
    t_start = time.time()
    textList = glob.glob(READ_PATH)
    for each_file in textList:
        print each_file
        plaza_count(each_file)
    t_end = time.time()
    print 'cost %f sec' % (t_end - t_start)
    print 'ending...'

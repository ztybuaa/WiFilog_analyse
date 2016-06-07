#-*- coding: utf-8 -*-
"""plaza_interval_time"""

import string
import csv
import re
import glob
import time
import collections
from tools.interval_time import nearby_difference_list

READ_PATH = r'result/weblog_*_preprocessed.csv'
SAVE_PATH = r'result/plaza_interval_time.csv'
plazas = ['1000269']

def plaza_interval_time(name):    
    result = {}
    reader = csv.reader(open(name, 'rb'))
    for line in reader:
        plaza = str(line[5])
        if plaza in plazas:
            if plaza not in result.keys():
                result[plaza] = {}
                result[plaza]['ts'] = []
                result[plaza]['ts'].append(int(line[1]))
            else:
                result[plaza]['ts'].append(int(line[1]))

    for plaza in result:
        num = len(result[plaza]['ts'])
        result[plaza]['ts'].sort()
        result[plaza]['interval_time'] = {}
        if num > 1:
            nearby_data = nearby_difference_list(result[plaza]['ts'])
            collection = collections.Counter(nearby_data)
            for each in collection:
                result[plaza]['interval_time'][each] = collection[each]                
           
                    
    with open(SAVE_PATH, 'ab') as f:
        writer = csv.writer(f)
        for plaza in result:
            #writer.writerow([plaza])
            for each in result[plaza]['interval_time']:
                writer.writerow([each, result[plaza]['interval_time'][each]])
        f.close()        

if __name__ == '__main__':
    print 'starting...'
    t_start = time.time()
    textList = glob.glob(READ_PATH)
    for each_file in textList:
        print each_file
        plaza_interval_time(each_file)
    t_end = time.time()
    print 'cost %f sec' % (t_end - t_start)
    print 'ending...'

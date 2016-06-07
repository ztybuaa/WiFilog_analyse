#-*- coding: utf-8 -*-
"""data_summarize"""

import string
import csv
import re
import glob
import time
from tools.brand import brand_trans

READ_PATH = r'result/weblog_*_preprocessed.csv'
SAVE_PATH = 'result/data_sum.csv'

def data_summarize(name):
    result = []
    reader = csv.reader(open(name, 'rb'))
    for line in reader:
        if str(line[1]) != 'time' and str(line[0]) != '' and str(line[5]) != '':
            line[10] = brand_trans(str(line[10]))
            result.append([line[0], line[1], line[5], line[7], line[9], line[10]])        

    with open(SAVE_PATH, 'ab') as f:
        writer = csv.writer(f)
        for each in result:
            writer.writerow(each)
        f.close()        

if __name__ == '__main__':
    print 'starting...'
    t_start = time.time()
    textList = glob.glob(READ_PATH)
    for each_file in textList:
        print each_file
        data_summarize(each_file)
    t_end = time.time()
    print 'cost %f sec' % (t_end - t_start)
    print 'ending...'

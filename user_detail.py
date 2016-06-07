 #-*- coding: utf-8 -*-
"""user_detail"""

import string
import csv
import glob
import time

READ_PATH = r'result/weblog_*_preprocessed.csv'
cmacs = ['3CA34897D6FA']

def time_trans(string):
    return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(float(string)))
    
def user_detail(name):
    '''根据cmac查询'''
    result = {}
    for cmac in cmacs:
        result[cmac] = []
        
    reader = csv.reader(open(name, 'rb'))
    for line in reader:
        cmac = str(line[0])
        if cmac in cmacs:
            result[cmac].append([line[0], time_trans(line[1]), line[5], line[6], line[7], line[10]])            

    for cmac in cmacs:                
        with open('result/%s_detail.csv' % cmac, 'ab') as f:
            writer = csv.writer(f)
            for line in result[cmac]:
                writer.writerow(line)
        f.close()        

if __name__ == '__main__':
    print 'starting...'
    t_start = time.time()
    textList = glob.glob(READ_PATH)
    for each_file in textList:
        print each_file
        user_detail(each_file)
    t_end = time.time()
    print 'cost %f sec' % (t_end - t_start)
    print 'ending...'

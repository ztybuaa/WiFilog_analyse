#-*- coding: utf-8 -*-
"""redirect_analyse"""

import string
import csv
import re
import time

READ_PATH = r'result/data_sum.csv'
SAVE_PATH = r'result/redirect_analyse.txt'

def redirect_analyse(name):
    '''重定向地址分析'''
    redirect_re = re.compile(r'(.*?)/')
    reader = csv.reader(open(name, 'rb'))
    f = open(SAVE_PATH, 'ab')
    for line in reader:
        try:
            line[4] = line[4].replace('.com','.com/').replace('.cn','.cn/')
            redirect = redirect_re.findall(line[4])[0]
            f.write(str(redirect)+'\n')
        except Exception,e:
            t = open('result/redirect_analyse_log.txt', 'ab')
            t.write(line[4]+'\n')
            t.close()
    f.close()

if __name__ == '__main__':
    print 'starting...'
    t_start = time.time()
    redirect_analyse(READ_PATH)
    t_end = time.time()
    print 'cost %f sec' % (t_end - t_start)
    print 'ending...'

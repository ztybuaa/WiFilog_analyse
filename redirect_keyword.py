#-*- coding: utf-8 -*-
"""redirect_keyword"""

import string
import time
import csv

READ_PATH = r'result/redirect_analyse.txt'
SAVE_PATH = r'result/redirect_keyword.txt'

def redirect_keyword(name):
    f = open(name, 'rb')
    words = []
    for line in f:
        words.extend(line.strip().split(' '))

    result = {}
    for word in words:
        if word in result:
            result[word] += 1
        else:
            result[word] = 1

    '''写文件'''
    f = open(SAVE_PATH,'ab')
    for item in result:
        f.write(item+' '+str(result[item])+'\n')
    f.write('\n')
    f.close()
    
if __name__ == '__main__':
    print 'redirect_keyword starting...'
    t_start = time.time()
    redirect_keyword(READ_PATH)
    t_end = time.time()
    print 'cost %f sec' % (t_end - t_start)
    print 'ending...'
    

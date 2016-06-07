#-*- coding: utf-8 -*-
"""url_keyword"""

import string
import time
import csv
import glob

READ_PATH = r'result/url_analyse.txt'
SAVE_PATH = r'result/url_keyword.txt'

def url_keyword(name):
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
    f = open(SAVE_PATH, 'wb')
    for item in result:
        f.write(item+' '+str(result[item])+'\n')
    f.write('\n')
    f.close()
    
if __name__ == '__main__':
    print 'starting...'
    t_start = time.time()
    url_keyword(READ_PATH)
    t_end = time.time()
    print 'cost %f sec' % (t_end - t_start)
    print 'ending...'
    

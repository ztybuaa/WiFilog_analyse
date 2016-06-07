#-*- coding: utf-8 -*-
"""url_analyse"""

import string
import csv
import re
import time

READ_PATH = r'result/data_sum.csv'
SAVE_PATH = r'result/url_analyse.txt'
PLAZA_ID = '1000269'

def url_analyse(name):
    url_re = re.compile(r'http.*?://(.*?)/')
    reader = csv.reader(open(name, 'rb'))
    f = open(SAVE_PATH, 'ab')
    n = 0
    for line in reader:
        n += 1
        if n % 100000 == 0:
            print n
        if line[3] != '' and str(line[2]) == PLAZA_ID:
            try:
                line[3] = line[3].replace('"','').replace('.com','.com/').replace('.cn','.cn/')
                url = url_re.findall(line[3])[0]
                #redirect_split = redirect.split('.')
                #for word in redirect_split:
                    #f.write(str(word)+' ')
                f.write(str(url)+' ')
                f.write('\n')
            except Exception,e:
                t = open('result/url_analyse_log.txt', 'ab')
                t.write(line[3]+'\n')
                t.close()
    f.close()

if __name__ == '__main__':
    print 'url analyse starting...'
    t_start = time.time()
    url_analyse(READ_PATH)
    t_end = time.time()
    print 'cost %f sec' % (t_end - t_start)
    print 'ending...'

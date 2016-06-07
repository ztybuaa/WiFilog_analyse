 #-*- coding: utf-8 -*-
"""plaza_adclick"""

import string
import csv
import glob
import time

READ_PATH = r'result/weblog_*_preprocessed.csv'
SAVE_PATH = r'result/plaza_adclick.csv'

def plaza_adclick(name):
    urls = {'game':'zhan.51h5.com', 'movie':'moviedetail', 'store':'storedetail', \
            'coupon':'coupondetail', 'share':'service.weibo.com'}
    result = {}
    reader = csv.reader(open(name, 'rb'))
    for line in reader:
        plaza = str(line[5])
        if plaza != 'plaza_id' and plaza != '' and str(line[0]) != '':
            if plaza not in result.keys():
                result[plaza] = {}
                for url in urls:
                    result[plaza][url] = 0
                    if urls[url] in str(line[7]):
                        result[plaza][url] += 1
            else:
                for url in urls:
                    if urls[url] in str(line[7]):
                        result[plaza][url] += 1            
                    
    with open(SAVE_PATH, 'ab') as f:
        writer = csv.writer(f)
        writer.writerow(['date', str(name)])
        for plaza in result:
            line = []
            line.append(plaza)
            line.append(result[plaza]['game'])
            line.append(result[plaza]['movie'])
            line.append(result[plaza]['store'])
            line.append(result[plaza]['coupon'])
            line.append(result[plaza]['share'])
            writer.writerow(line)
        f.close()        

if __name__ == '__main__':
    print 'starting...'
    t_start = time.time()
    textList = glob.glob(READ_PATH)
    for each_file in textList:
        print each_file
        plaza_adclick(each_file)
    t_end = time.time()
    print 'cost %f sec' % (t_end - t_start)
    print 'ending...'

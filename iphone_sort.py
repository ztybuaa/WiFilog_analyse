#-*- coding: utf-8 -*-
"""iphone_sort"""

import string
import csv
import time
from tools.time_format import time_trans

READ_PATH = r'result/data_sum.csv'
SAVE_PATH = r'result/iphone_sort.csv'

def iphone_sort(name):
    brands = ['iPad', 'iPod', 'iPhone', \
              'iPhone 4', 'iPhone 4s', 'iPhone 5', 'iPhone 5s', 'iPhone 5c', \
              'iPhone 6', 'iPhone 6p', 'iPhone 6s', 'iPhone 6sp', \
              'Macintosh']
    urls = {'game':'zhan.51h5.com', 'movie':'moviedetail', \
            'store':'storedetail', 'share':'service.weibo.com'}

    result = {}
    #初始化result
    for brand in brands:
        result[brand] = {}
        result[brand]['cmac'] = []
        result[brand]['login_time'] = []
        for url in urls:
            result[brand][url] = 0
        
    reader = csv.reader(open(name, 'rb'))
    n = 0
    for line in reader:
        n += 1
        if n % 100000 == 0:
            print n
        brand = str(line[5])
        if brand in brands:
            result[brand]['cmac'].append(str(line[0]))
            result[brand]['login_time'].append(float(time_trans(line[1])))
            for url in urls:
                if urls[url] in str(line[3]):
                    result[brand][url] += 1

    for brand in brands:        
        result[brand]['num_click'] = len(result[brand]['cmac'])
        result[brand]['num_cmac'] = len(set(result[brand]['cmac']))
        if len(result[brand]['login_time']) != 0:
            result[brand]['login_time'] = sum(result[brand]['login_time']) * 1.0 / len(result[brand]['login_time'])
        else:
            result[brand]['login_time'] = 0

    with open(SAVE_PATH, 'wb') as f:
        writer = csv.writer(f)
        for brand in result:
            line = []
            line.append(brand)
            line.append(result[brand]['num_click'])
            line.append(result[brand]['num_cmac'])
            line.append(result[brand]['login_time'])
            line.append(result[brand]['game'])
            line.append(result[brand]['movie'])
            line.append(result[brand]['store'])
            line.append(result[brand]['share'])
            writer.writerow(line)
        f.close()

if __name__ == '__main__':
    print 'starting...'
    t_start = time.time()
    iphone_sort(READ_PATH)
    t_end = time.time()
    print 'cost %f sec' % (t_end - t_start)
    print 'ending...'

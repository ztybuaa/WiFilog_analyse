#-*- coding: utf-8 -*-
"""plaza_device"""

import string
import csv
import time
from tools.brand import brand_trans

READ_PATH = r'result/data_sum.csv'
SAVE_PATH = r'result/plaza_device.csv'

def plaza_device(name):
    '''各广场设备品牌'''
    brands = ['iPad', 'iPod', 'iPhone', 'vivo', 'MI', \
              'HUAWEI', 'OPPO', 'SAMSUNG', 'Coolpad', \
              'Lenovo', 'HTC', 'Letv', 'ZTE', 'LG', 'dazen',\
              'Nokia', 'AMOI', 'Meizu', 'sony', \
              'TCL', 'ASUS', 'Hisense', 'Changhong', \
              'Macintosh', 'Windows NT', 'others']
    result = {}
    reader = csv.reader(open(name, 'rb'))
    n = 0
    for line in reader:
        n += 1
        if n % 100000 == 0:
            print n
        plaza = str(line[2])
        if int(plaza) <= 1000773:
            if plaza not in result.keys():
                result[plaza] = {}
                for brand in brands:
                    result[plaza][brand] = []
                    if brand_trans(str(line[5])) == brand:
                        result[plaza][brand].append(str(line[0]))
            else:
                for brand in brands:
                    if brand_trans(str(line[5])) == brand:
                        result[plaza][brand].append(str(line[0]))
                    
    with open(SAVE_PATH, 'wb') as f:
        writer = csv.writer(f)
        writer.writerow(['plaza', \
                         'iPad', 'iPod', 'iPhone', 'vivo', 'MI', \
                         'HUAWEI', 'OPPO', 'SAMSUNG', 'Coolpad', \
                         'Lenovo', 'HTC', 'Letv', 'ZTE', 'LG', 'dazen',\
                         'Nokia', 'AMOI', 'Meizu', 'sony', \
                         'TCL', 'ASUS', 'Hisense', 'Changhong', \
                         'Macintosh', 'Windows NT', 'others'])
        for plaza in result:
            line = []
            line.append(plaza)
            for brand in brands:
                line.append(len(set(result[plaza][brand])))
            writer.writerow(line)
        f.close()        

if __name__ == '__main__':
    print 'starting...'
    t_start = time.time()
    plaza_device(READ_PATH)
    t_end = time.time()
    print 'cost %f sec' % (t_end - t_start)
    print 'ending...'

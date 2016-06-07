#-*- coding: utf-8 -*-
"""plaza_feature"""

import string
import csv
import re
import glob
import time
from tools.time_format import time_trans
from tools.brand import brand_trans, brand_var, brand_count
from tools.interval_time import entropy, nearby_difference_list
from numpy import var

READ_PATH = r'result/weblog_*_preprocessed.csv'
SAVE_PATH = r'result/plaza_feature.csv'

def plaza_feature(name):
    '''计算广场的设备比例方差、平均点击时间、点击时间方差、平均点击间隔、点击间隔信息熵、主要品牌数'''
    result = {}
    reader = csv.reader(open(name, 'rb'))
    for line in reader:
        plaza = str(line[5])
        if plaza != 'plaza_id' and plaza != '' and str(line[0]) != '':
            if plaza not in result.keys():
                result[plaza] = {}
                result[plaza]['terminal'] = []
                result[plaza]['ts'] = []
                if str(line[10]) != '':
                    result[plaza]['terminal'].append(str(line[10]))
                result[plaza]['ts'].append(int(line[1]))
            else:
                if str(line[10]) != '':
                    result[plaza]['terminal'].append(str(line[10]))
                result[plaza]['ts'].append(int(line[1]))

    for plaza in result:
        result[plaza]['terminal'] = brand_trans(result[plaza]['terminal'])
        result[plaza]['brand_var'] = brand_var(result[plaza]['terminal'])
        result[plaza]['sum_proportion0.5'] = brand_count(result[plaza]['terminal'], 0.5)
        num = len(result[plaza]['ts'])
        result[plaza]['ts'].sort()
        if num > 1:
            result[plaza]['average_login_time'] = time_trans(sum(result[plaza]['ts']) * 1.0 / num)
            result[plaza]['var_login_time'] = var(result[plaza]['ts'])
            nearby_data = nearby_difference_list(result[plaza]['ts'])
            result[plaza]['average_nearby_time'] = sum(nearby_data) * 1.0 / len(nearby_data)
            result[plaza]['entropy_nearby_time'] = entropy(nearby_data)
        else:
            result[plaza]['average_login_time'] = ''
            result[plaza]['var_login_time'] = ''
            result[plaza]['average_nearby_time'] = ''
            result[plaza]['entropy_nearby_time'] = ''            
                    
    with open(SAVE_PATH, 'ab') as f:
        writer = csv.writer(f)
        writer.writerow([str(name), \
                         'brand_var', 'average_login_time', 'var_login_time', \
                         'average_nearby_time', 'entropy_nearby_time', 'sum_proportion0.5'])
        for plaza in result:
            line = []
            line.append(plaza)
            line.append(result[plaza]['brand_var'])
            line.append(result[plaza]['average_login_time'])
            line.append(result[plaza]['var_login_time'])
            line.append(result[plaza]['average_nearby_time'])
            line.append(result[plaza]['entropy_nearby_time'])
            line.append(result[plaza]['sum_proportion0.5'])
            writer.writerow(line)
        f.close()        

if __name__ == '__main__':
    print 'starting...'
    t_start = time.time()
    textList = glob.glob(READ_PATH)
    for each_file in textList:
        print each_file
        plaza_feature(each_file)
    t_end = time.time()
    print 'cost %f sec' % (t_end - t_start)
    print 'ending...'

#-*- coding: utf-8 -*-
"""user_sort"""

import string
import csv
import re
import time
import collections
import numpy
from tools.brand import brand_trans
from tools.time_format import time_trans, date_trans
from tools.interval_time import entropy, nearby_difference_list

READ_PATH = r'result/data_sum.csv'
SAVE_PATH = r'result/user_result.csv'

def user_sort(name):
    urls = {'game':'zhan.51h5.com', 'movie':'moviedetail', 'store':'storedetail'}
    cmacs = {}
    reader = csv.reader(open(name, 'rb'))
    n = 0
    for line in reader:
        n += 1
        if n % 100000 == 0:
            print n
        if str(line[5]) != '':
            cmac = str(line[0])
            if cmac not in cmacs.keys():
                cmacs[cmac] = {}
                cmacs[cmac]['ts'] = {}
                date = date_trans(line[1])
                cmacs[cmac]['ts'][date] = []
                cmacs[cmac]['ts'][date].append(line[1])
                cmacs[cmac]['plaza'] = []
                cmacs[cmac]['plaza'].append(str(line[2]))
                for url in urls:
                    cmacs[cmac][url] = 0
                    if urls[url] in str(line[3]):
                        cmacs[cmac][url] += 1
                cmacs[cmac]['terminal'] = str(line[5])
            else:
                date = date_trans(line[1])
                if date not in cmacs[cmac]['ts'].keys():
                    cmacs[cmac]['ts'][date] = []
                    cmacs[cmac]['ts'][date].append(line[1])
                else:
                    cmacs[cmac]['ts'][date].append(line[1])
                if str(line[2]) not in cmacs[cmac]['plaza']:
                    cmacs[cmac]['plaza'].append(str(line[2]))
                for url in urls:
                    if urls[url] in str(line[3]):
                        cmacs[cmac][url] += 1

    for cmac in cmacs:
        #计算登录天数、点击次数
        cmacs[cmac]['checkin_days'] = len(cmacs[cmac]['ts'])
        count = 0
        for day in cmacs[cmac]['ts']:
            count += len(cmacs[cmac]['ts'][day])
        cmacs[cmac]['checkin_count'] = count

        #计算登录时间的最大值、最小值、均值、中位数
        checkin_time = []
        for day in cmacs[cmac]['ts']:
            for ts in cmacs[cmac]['ts'][day]:
                time = time_trans(ts)
                checkin_time.append(time)
        checkin_time.sort()
        cmacs[cmac]['early_time'] = checkin_time[0]
        cmacs[cmac]['late_time'] = checkin_time[-1]
        cmacs[cmac]['average_checkin_time'] = numpy.mean(checkin_time)
        cmacs[cmac]['median_checkin_time'] = numpy.median(checkin_time)

        #计算每天平均停留时间、平均点击间隔时间、点击间隔时间信息熵
        duration = []
        average_interval_time = []
        entropy_interval_time = []        
        for day in cmacs[cmac]['ts']:
            ts_list = cmacs[cmac]['ts'][day]
            ts_list.sort()
            ts_list_length = len(ts_list)
            if ts_list_length >= 2:
                duration.append(int(ts_list[-1])-int(ts_list[0]))
                day_interval_time_list = nearby_difference_list(ts_list)
                average_interval_time.append(numpy.mean(day_interval_time_list))
                entropy_interval_time.append(entropy(day_interval_time_list))
            else:
                duration.append(0)
                average_interval_time.append(0)
                entropy_interval_time.append(0)
        cmacs[cmac]['average_duration'] = numpy.mean(duration)
        cmacs[cmac]['average_interval_time'] = numpy.mean(average_interval_time)
        cmacs[cmac]['entropy_interval_time'] = numpy.mean(entropy_interval_time)
               
    with open(SAVE_PATH, 'wb') as f:
        writer = csv.writer(f)
        writer.writerow(['cmac', 'checkin_days', 'checkin_count', 'early_time', 'late_time', \
                         'average_duration', 'average_checkin_time', 'median_checkin_time', \
                         'average_interval_time', 'entropy_interval_time', \
                         'plaza', 'terminal', 'game', 'movie', 'store'])
        for cmac in cmacs:
            line = []
            line.append(cmac)
            items = ['checkin_days', 'checkin_count', 'early_time', 'late_time', \
                     'average_duration', 'average_checkin_time', 'median_checkin_time', \
                     'average_interval_time', 'entropy_interval_time', \
                     'plaza', 'terminal', 'game', 'movie', 'store']
            for item in items:
                line.append(cmacs[cmac][item])
            writer.writerow(line)
        f.close()        

if __name__ == '__main__':
    print 'starting...'
    t_start = time.time()
    user_sort(READ_PATH)
    t_end = time.time()
    print 'cost %f sec' % (t_end - t_start)
    print 'ending...'

#-*- coding: utf-8 -*-
"""day_hour_analyse"""

import string
import csv
import glob
import time
from tools.interval_time import entropy, nearby_difference_list
from tools.time_format import hour_day_trans

READ_PATH = r'result/weblog_*_preprocessed.csv'
SAVE_PATH = r'result/day_hour_analyse.csv'

def day_hour_analyse(name):
    urls = {'game':'zhan.51h5.com', 'movie':'moviedetail', \
            'store':'storedetail', 'share':'service.weibo.com'}
    result = {}
    #result = {'Mon':{'00':{'cmac':[],'ts':[],'game':0,'movie':0,'store':0,'share':0}}}
    reader = csv.reader(open(name, 'rb'))
    for line in reader:
        if line[0] != '' and line[1] != 'time':
            hour_day = hour_day_trans(line[1])
            hour = hour_day[0]
            day = hour_day[1]
            if day not in result.keys():
                result[day] = {}
                result[day][hour] = {}
                result[day][hour]['cmac'] = []
                result[day][hour]['ts'] = []
                for url in urls:
                    result[day][hour][url] = 0
                    if urls[url] in str(line[7]):
                        result[day][hour][url] += 1
                result[day][hour]['cmac'].append(str(line[0]))
                result[day][hour]['ts'].append(int(line[1]))
            else:
                if hour not in result[day].keys():
                    result[day][hour] = {}
                    result[day][hour]['cmac'] = []
                    result[day][hour]['ts'] = []
                    for url in urls:
                        result[day][hour][url] = 0
                        if urls[url] in str(line[7]):
                            result[day][hour][url] += 1
                    result[day][hour]['cmac'].append(str(line[0]))
                    result[day][hour]['ts'].append(int(line[1]))
                else:
                    for url in urls:
                        if urls[url] in str(line[7]):
                            result[day][hour][url] += 1
                    result[day][hour]['cmac'].append(str(line[0]))
                    result[day][hour]['ts'].append(int(line[1]))

    for day in result:
        for hour in result[day]:
            result[day][hour]['num_cmac'] = len(set(result[day][hour]['cmac']))
            result[day][hour]['ts'].sort()
            result[day][hour]['count'] = len(result[day][hour]['ts'])
            if result[day][hour]['count'] > 1:
                nearby_data = nearby_difference_list(result[day][hour]['ts'])
                result[day][hour]['average_interval_time'] = sum(nearby_data) * 1.0 / len(nearby_data)
                result[day][hour]['entropy_interval_time'] = entropy(nearby_data)
            else:
                result[day][hour]['average_interval_time'] = ''
                result[day][hour]['entropy_interval_time'] = ''
                                 
    with open(SAVE_PATH, 'ab') as f:
        writer = csv.writer(f)
        writer.writerow([str(name), \
                         'hour', 'num_cmac', 'count', 'average_interval_time', \
                         'entropy_interval_time', 'game', 'movie', 'store', 'share'])
        for day in result:
            for hour in result[day]:
                line = []
                line.append(day)
                line.append(hour)
                line.append(result[day][hour]['num_cmac'])
                line.append(result[day][hour]['count'])
                line.append(result[day][hour]['average_interval_time'])
                line.append(result[day][hour]['entropy_interval_time'])
                line.append(result[day][hour]['game'])
                line.append(result[day][hour]['movie'])
                line.append(result[day][hour]['store'])
                line.append(result[day][hour]['share'])
                writer.writerow(line)
        f.close()        

if __name__ == '__main__':
    print 'starting...'
    t_start = time.time()
    textList = glob.glob(READ_PATH)
    for each_file in textList:
        print each_file
        day_hour_analyse(each_file)
    t_end = time.time()
    print 'cost %f sec' % (t_end - t_start)
    print 'ending...'

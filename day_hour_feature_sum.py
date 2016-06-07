#-*- coding: utf-8 -*-
"""day_hour_analyse_sum"""

import string
import csv
import time

READ_PATH = r'result/day_hour_analyse.csv'
SAVE_PATH = r'result/day_hour_analyse_sum.csv'

def day_hour_analyse_sum(name):
    weeks = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    result = {}
    reader = csv.reader(open(name, 'rb'))
    for line in reader:
        if str(line[0]) in weeks:
            day_hour = str(line[0]) + str(line[1])
            try:
                if day_hour not in result.keys():
                    result[day_hour] = {}
                    result[day_hour]['num_cmac'] = int(line[2])
                    result[day_hour]['count'] = int(line[3])
                    result[day_hour]['average_interval_time'] = float(line[4])
                    result[day_hour]['entropy_interval_time'] = float(line[5])
                    result[day_hour]['game'] = int(line[6])
                    result[day_hour]['movie'] = int(line[7])
                    result[day_hour]['store'] = int(line[8])
                    result[day_hour]['share'] = int(line[9])
                else:
                    result[day_hour]['num_cmac'] += int(line[2])
                    result[day_hour]['count'] += int(line[3])
                    result[day_hour]['average_interval_time'] += float(line[4])
                    result[day_hour]['entropy_interval_time'] += float(line[5])
                    result[day_hour]['game'] += int(line[6])
                    result[day_hour]['movie'] += int(line[7])
                    result[day_hour]['store'] += int(line[8])
                    result[day_hour]['share'] += int(line[9])
            except Exception,e:
                print e
                print line

    for day_hour in result:
        for item in result[day_hour]:
            result[day_hour][item] = result[day_hour][item] * 1.0 / 29        
         
    with open(SAVE_PATH, 'ab') as f:
        writer = csv.writer(f)
        writer.writerow(['day_hour','num_cmac', 'count', 'average_interval_time', \
                         'entropy_interval_time', 'game', 'movie', 'store', 'share'])
        for day_hour in result:
            line = []
            line.append(day_hour)
            line.append(result[day_hour]['num_cmac'])
            line.append(result[day_hour]['count'])
            line.append(result[day_hour]['average_interval_time'])
            line.append(result[day_hour]['entropy_interval_time'])
            line.append(result[day_hour]['game'])
            line.append(result[day_hour]['movie'])
            line.append(result[day_hour]['store'])
            line.append(result[day_hour]['share'])
            writer.writerow(line)
        f.close()        

if __name__ == '__main__':
    print 'starting...'
    t_start = time.time()
    day_hour_analyse_sum(READ_PATH)
    t_end = time.time()
    print 'cost %f sec' % (t_end - t_start)
    print 'ending...'

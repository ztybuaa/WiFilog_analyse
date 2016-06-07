#-*- coding: utf-8 -*-
"""plaza_count_sum"""

import string
import csv
import time

READ_PATH = r'result/plaza_count.csv'
SAVE_PATH = r'result/plaza_count_sum.csv'
N = 3 #days

def plaza_count_sum(name):
    result = {}
    reader = csv.reader(open(name, 'rb'))
    for line in reader:
        if str(line[0]) != 'date':
            plaza = str(line[0])
            if plaza not in result.keys():
                result[plaza] = {}
                result[plaza]['count'] = []
                result[plaza]['during'] = []
                result[plaza]['num_cmac'] = []
                
                result[plaza]['count'].append(float(line[1]))
                result[plaza]['during'].append(float(line[2]))
                result[plaza]['num_cmac'].append(int(line[3]))
            else:
                result[plaza]['count'].append(float(line[1]))
                result[plaza]['during'].append(float(line[2]))
                result[plaza]['num_cmac'].append(int(line[3]))

    average_count = {}
    average_during = {}
    average_num_cmac = {}
    for plaza in result:
        if len(result[plaza]['count']) == N:
            total_count = 0      
            for count in result[plaza]['count']:
                total_count += float(count)
            average_count[plaza] = total_count * 1.0 / len(result[plaza]['count'])

            total_during = 0
            for during in result[plaza]['during']:
                total_during += float(during)
            average_during[plaza] = total_during * 1.0 / len(result[plaza]['during'])

            total_num_cmac = 0
            for num_cmac in result[plaza]['num_cmac']:
                total_num_cmac += int(num_cmac)
            average_num_cmac[plaza] = total_num_cmac * 1.0 #/ len(result[plaza]['num_cmac'])
         
    with open(SAVE_PATH, 'ab') as f:
        writer = csv.writer(f)
        for plaza in average_count:
            line = []
            line.append(plaza)
            line.append(average_count[plaza])
            line.append(average_during[plaza])
            line.append(average_num_cmac[plaza])
            writer.writerow(line)
        f.close()        

if __name__ == '__main__':
    print 'starting...'
    t_start = time.time()
    plaza_count_sum(READ_PATH)
    t_end = time.time()
    print 'cost %f sec' % (t_end - t_start)
    print 'ending...'

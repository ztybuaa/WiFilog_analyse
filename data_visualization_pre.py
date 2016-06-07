#-*- coding: utf-8 -*-
"""data_visualization_pre"""

import string
import csv
import re
import glob
import time
from tools.brand import brand_trans
from tools.time_format import hour_trans, date_trans

READ_PATH = r'result/weblog_*_preprocessed.csv'

def data_visualization_pre(name):
    '''可视化数据准备'''
    urls = {'game':'zhan.51h5.com', 'movie':'moviedetail', \
            'store':'storedetail', 'share':'service.weibo.com'}
    brands = ['iPhone', 'SAMSUNG', 'vivo', 'MI', 'HUAWEI', 'OPPO', 'Lenovo', 'Coolpad', 'Meizu']
    result = {}
    reader = csv.reader(open(name, 'rb'))
    for line in reader:
        if line[0] != '' and line[1] != 'time':
            plaza = line[5]
            date = date_trans(line[1])
            hour = hour_trans(line[1])
            if plaza not in result.keys():
                result[plaza] = {}
                result[plaza][hour] = {}
                result[plaza][hour]['cmac'] = []
                result[plaza][hour]['ts'] = []
                result[plaza][hour]['cmac'].append(str(line[0]))
                result[plaza][hour]['ts'].append(str(line[1]))
                for url in urls:
                    result[plaza][hour][url] = 0
                    if urls[url] in str(line[7]):
                        result[plaza][hour][url] += 1
                for brand in brands:
                    result[plaza][hour][brand] = 0
                    if brand_trans(str(line[10])) == brand:
                        result[plaza][hour][brand] += 1
            else:
                if hour not in result[plaza].keys():
                    result[plaza][hour] = {}
                    result[plaza][hour]['cmac'] = []
                    result[plaza][hour]['ts'] = []
                    result[plaza][hour]['cmac'].append(str(line[0]))
                    result[plaza][hour]['ts'].append(str(line[1]))
                    for url in urls:
                        result[plaza][hour][url] = 0
                        if urls[url] in str(line[7]):
                            result[plaza][hour][url] += 1
                    for brand in brands:
                        result[plaza][hour][brand] = 0
                        if brand_trans(str(line[10])) == brand:
                            result[plaza][hour][brand] += 1
                else:
                    if str(line[0]) not in result[plaza][hour]['cmac']:
                        result[plaza][hour]['cmac'].append(str(line[0]))
                        for brand in brands:
                            if brand_trans(str(line[10])) == brand:
                                result[plaza][hour][brand] += 1
                                break
                    result[plaza][hour]['ts'].append(str(line[1]))
                    for url in urls:
                        if urls[url] in str(line[7]):
                            result[plaza][hour][url] += 1
                            break

    for plaza in result:
        for hour in result[plaza]:
            result[plaza][hour]['num_cmac'] = len(result[plaza][hour]['cmac'])
            result[plaza][hour]['count'] = len(result[plaza][hour]['ts'])
        with open('result/plaza/%s.csv' % str(plaza), 'ab') as f:
            writer = csv.writer(f)
            '''writer.writerow(['date', 'hour', 'num_cmac', 'count', \
                             'game', 'movie', 'store', 'share', \
                             'iPhone', 'SAMSUNG', 'vivo', 'MI', \
                             'HUAWEI', 'OPPO', 'Lenovo', 'Coolpad', 'Meizu'])
            '''
            for hour in range(0,24):
                if hour < 10:
                    hour = '0' + str(hour)
                else:
                    hour = str(hour)
                line = []
                line.append(date)
                line.append(hour)
                if hour in result[plaza].keys():
                    line.append(result[plaza][hour]['num_cmac'])
                    line.append(result[plaza][hour]['count'])
                    line.append(result[plaza][hour]['game'])
                    line.append(result[plaza][hour]['movie'])
                    line.append(result[plaza][hour]['store'])
                    line.append(result[plaza][hour]['share'])
                    line.append(result[plaza][hour]['iPhone'])
                    line.append(result[plaza][hour]['SAMSUNG'])
                    line.append(result[plaza][hour]['vivo'])
                    line.append(result[plaza][hour]['MI'])
                    line.append(result[plaza][hour]['HUAWEI'])
                    line.append(result[plaza][hour]['OPPO'])
                    line.append(result[plaza][hour]['Lenovo'])
                    line.append(result[plaza][hour]['Coolpad'])
                    line.append(result[plaza][hour]['Meizu'])
                else:
                    line.extend([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
                writer.writerow(line)
            f.close()     

if __name__ == '__main__':
    print 'starting...'
    t_start = time.time()
    textList = glob.glob(READ_PATH)
    for each_file in textList:
        print each_file
        data_visualization_pre(each_file)
    t_end = time.time()
    print 'cost %f sec' % (t_end - t_start)
    print 'ending...'

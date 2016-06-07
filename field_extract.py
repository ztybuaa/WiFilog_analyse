#-*- coding: utf-8 -*-
"""field_extract"""

import string
import csv
import re
import glob
import time
from tools.time_format import ts_trans as tt
from tools.brand import brand_extract as be

READ_PATH = r'result/weblog_*_cleaned.csv'

def field_extract(name):
    '''字段整理'''
    CMACs = {}
    reader = csv.reader(open(name, 'rb'))
    for line in reader:
        if str(line[6]) != '' and str(line[6]) != 'plaza_id':
            time = tt(line[1])
            CMAC = line[2]
            SID = line[3]
            new_mac_flag = line[4]
            uid = str(line[5])
            plaza_id = line[6]
            city_id = line[8]
            url = line[13]
            switch_url = line[14]
            redirect = line[15]
            if line[16] != '[]':
                terminal = be(line[16])
            else:
                terminal = ''
            if CMAC not in CMACs.keys():
                CMACs[CMAC] = []
                CMACs[CMAC].append([time, uid, SID, new_mac_flag, plaza_id, city_id, url, switch_url, redirect, terminal])
            else:
                CMACs[CMAC].append([time, uid, SID, new_mac_flag, plaza_id, city_id, url, switch_url, redirect, terminal])
    return CMACs

def user_count(data, name):
    '''点击统计'''
    result = []
    for line in data:
        item = []
        CMAC = line
        plaza_id = data[line][0][4]
        count = len(data[line])
        early_ts = late_ts = data[line][0][0]
        for row in data[line]:
            if row[0] < early_ts:
                early_ts = row[0]
            if row[0] > late_ts:
                late_ts = row[0]
        during = late_ts - early_ts
        item = [CMAC, plaza_id, count, early_ts, late_ts, during]
        result.append(item)
    with open('result/%s_count.csv' % str(name.replace('result\\','').replace('cleaned.csv','preprocessed')), 'wb') as f:
        writer = csv.writer(f)
        writer.writerow(['CMAC', 'plaza_id', 'count', 'early_ts', 'late_ts', 'during'])
        for line in result:
            writer.writerow(line)
        f.close()        
    
def write_csv(data, name):
    '''写数据'''
    with open('result/%s.csv' % str(name.replace('result\\','').replace('cleaned.csv','preprocessed')), 'wb') as f:
        writer = csv.writer(f)
        writer.writerow(['CMAC', 'time', 'uid', 'SID', 'new_mac_flag', 'plaza_id', 'city_id', 'url', 'switch_url', 'redirect', 'terminal'])
        for line in data:
            for row in data[line]:
                item = []
                item.append(line)
                item.extend(row)
                writer.writerow(item)
    f.close()

if __name__ == '__main__':
    print 'starting...'
    t_start = time.time()
    textList = glob.glob(READ_PATH)
    for each_file in textList:
        print each_file
        data = field_extract(each_file)
        user_count(data, each_file)
        write_csv(data, each_file)
    t_end = time.time()
    print 'cost %f sec' % (t_end - t_start)
    print 'ending...'

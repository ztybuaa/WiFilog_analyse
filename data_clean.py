#-*- coding: utf-8 -*-
"""data_clean"""

import string
import csv
import re
import glob
import time

READ_PATH = r'data/weblog_*'

def read_data(data):
    '''读文件'''
    text = []
    with open(data) as f:
        for line in f:
            text.append(str(line))
    f.close()
    return text

def data_clean(texts, name):
    '''字段提取'''
    ip_re = re.compile(r'\b(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\b', re.IGNORECASE)
    time_re = re.compile(r'\[(.*?)\]')
    CMAC_re = re.compile(r'CMAC=([a-zA-Z0-9]{12})')
    SID_re = re.compile(r'SID=([a-zA-Z0-9]{12})')
    new_mac_flag_re = re.compile(r'new_mac_flag=([0-1]{1})')
    uid_re = re.compile(r'uid=(\d+)')
    plaza_id_re = re.compile(r'PLAZA_ID=(\d+)')
    plaza_name_re = re.compile(r'PLAZA_NAME=([a-zA-Z0-9%]{81})')
    city_id_re = re.compile(r'CITY_ID=(\d+)')
    city_name_re = re.compile(r'CITY_NAME=([a-zA-Z0-9%]{27})')
    U_UID_re = re.compile(r'U_UID=([a-zA-Z0-9%]{26})')
    PHPSESSID_re = re.compile(r'PHPSESSID=([a-zA-Z0-9%]{32})')
    SESSIONID_re = re.compile(r'SESSIONID=([a-zA-Z0-9%]{32})')
    url_re = re.compile(r'url=(.*?) ')
    switch_url_re = re.compile(r'switch_url=(.*?)&')
    redirect_re = re.compile(r'redirect=(.*?) ')
    terminal_re = re.compile(r'\((.*?)\)')

    num = 0
    result = []
    for text in texts:
        num += 1

        item = {}
        try:
            item['ip'] = list(set(ip_re.findall(text)))
        except Exception, e:
            item['ip'] = ''

        try:
            item['time'] = time_re.findall(text)[0]
        except Exception, e:
            item['time'] = ''

        try:
            item['CMAC'] = CMAC_re.findall(text)[0]
        except Exception, e:
            item['CMAC'] = ''

        try:
            item['SID'] = list(set(SID_re.findall(text)))
        except Exception, e:
            item['SID'] = ''

        try:
            item['new_mac_flag'] = new_mac_flag_re.findall(text)[0]
        except Exception, e:
            item['new_mac_flag'] = ''

        try:
            item['uid'] = str(uid_re.findall(text)[0])
        except Exception, e:
            item['uid'] = ''

        try:
            item['plaza_id'] = plaza_id_re.findall(text)[0]
        except Exception, e:
            item['plaza_id'] = ''

        try:
            item['plaza_name'] = plaza_name_re.findall(text)[0]
        except Exception, e:
            item['plaza_name'] = ''

        try:
            item['city_id'] = city_id_re.findall(text)[0]
        except Exception, e:
            item['city_id'] = ''

        try:
            item['city_name'] = city_name_re.findall(text)[0]
        except Exception, e:
            item['city_name'] = ''

        try:
            item['U_UID'] = U_UID_re.findall(text)[0]
        except Exception, e:
            item['U_UID'] = ''

        try:
            item['PHPSESSID'] = PHPSESSID_re.findall(text)[0]
        except Exception, e:
            item['PHPSESSID'] = ''

        try:
            item['SESSIONID'] = SESSIONID_re.findall(text)[0]
        except Exception, e:
            item['SESSIONID'] = ''

        try:
            item['url'] = url_re.findall(text)[0].replace(
                '%3A', ':').replace('%2F', '/').replace('%2E', '.')
        except Exception, e:
            item['url'] = ''

        try:
            item['switch_url'] = switch_url_re.findall(text)[0].replace(
                '%3A', ':').replace('%2F', '/').replace('%2E', '.')
        except Exception, e:
            item['switch_url'] = ''

        try:
            item['redirect'] = redirect_re.findall(text)[0].replace(
                '%3A', ':').replace('%2F', '/').replace('%2E', '.')
        except Exception, e:
            item['redirect'] = ''

        try:
            item['terminal'] = terminal_re.findall(text)
        except Exception, e:
            item['terminal'] = ''
            
        result.append(item)
        
        if num % 10000 == 0 or num == len(texts): #10000条记录写一次数据
            print 'writing data...'
            write_csv(result, name)
            result = []


def write_begin(name):
    '''写表头'''
    with open('result/%s_cleaned.csv' % str(name.replace('data\\','')), 'wb') as f:
        writer = csv.writer(f)
        writer.writerow(['ip', 'time', 'CMAC', 'SID', 'new_mac_flag', 'uid', \
                         'plaza_id', 'plaza_name', 'city_id', 'city_name', 'U_UID', \
                         'PHPSESSID', 'SESSIONID', 'url', 'switch_url', 'redirect', 'terminal'])
    f.close()

def write_csv(data, name):
    '''写数据'''
    with open('result/%s_cleaned.csv' % str(name.replace('data\\','')), 'ab') as f:
        writer = csv.writer(f)
        for item in data:
            writer.writerow([item['ip'], item['time'], item['CMAC'], item['SID'], item['new_mac_flag'], \
                             item['uid'], item['plaza_id'], item['plaza_name'], item['city_id'], item['city_name'], \
                             item['U_UID'], item['PHPSESSID'], item['SESSIONID'], item['url'], item['switch_url'], item['redirect'], item['terminal']])
    f.close()

if __name__ == '__main__':
    print 'starting...'
    t_start = time.time()
    textList = glob.glob(READ_PATH)
    for each in textList:
        print each
        texts = read_data(each)
        write_begin(each)
        data_clean(texts, each)
    t_end = time.time()
    print 'cost %f sec' % (t_end - t_start)
    print 'ending...'

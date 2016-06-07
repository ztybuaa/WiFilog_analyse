#-*- coding: utf-8 -*-
"""time_format"""

import time
import re

def month_trans(data):
    '''月份转换'''
    mon = {'Jan':'01', 'Feb':'02', 'Mar':'03', 'Apr':'04', 'May':'05', 'Jun':'06', \
           'Jul':'07', 'Aug':'08', 'Sep':'09', 'Oct':'10', 'Nov':'11', 'Dec':'12'}
    if data in mon.keys():
        result = mon[data]
    else:
        result = ''
    return result
    
def time_format(data):
    '''时间格式转换'''
    split_time = re.split('[/: ]', data)
    year = split_time[2]
    month = month_trans(split_time[1])
    day = split_time[0]
    hour = split_time[3]
    minute = split_time[4]
    second = split_time[5]
    time_text = str(year) + '-' + str(month) + '-' + str(day) + ' ' + \
                str(hour) + ':' + str(minute) + ':' + str(second)
    return time_text

def ts_trans(data):
    '''时间转化成时间戳'''
    ts = int((time.mktime(time.strptime(time_format(data),'%Y-%m-%d %H:%M:%S'))))
    return ts

def time_trans(string):
    '''时间戳取时分秒并转化成秒数'''
    hms_time = time.strftime('%H:%M:%S', time.localtime(float(string)))
    split_time = hms_time.split(':')
    time_result = int(split_time[0]) * 3600.0 + int(split_time[1]) * 60.0 + int(split_time[2]) * 1.0
    return time_result

def date_trans(string):
    return time.strftime('%d', time.localtime(float(string)))

def hour_trans(string):
    str_hour = time.strftime("%H", time.localtime(float(string)))
    return str(str_hour)

def hour_day_trans(string):
    str_hour_day = time.strftime("%H %a", time.localtime(float(string)))
    return str_hour_day.split(' ')

def test():
    data = '19/Nov/2015:00:00:10 +0800'
    t = ts_trans(data)
    p = time_format(data)
    print p
    print t


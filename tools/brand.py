#-*- coding: utf-8 -*-
"""brand"""

import collections
from numpy import var

def brand_extract(string):
    '''提取设备品牌'''
    brands = ['iPhone 4', 'iPhone 4s', 'iPhone 5', 'iPhone 5s', 'iPhone 5c', \
              'iPhone 6', 'iPhone 6p', 'iPhone 6s', 'iPhone 6sp', 'iPad', 'iPod', \
              'iPhone', 'vivo', 'MI', 'HUAWEI', 'OPPO', 'SAMSUNG', 'Coolpad', \
              'Lenovo', 'HONOR', 'HTC', 'Letv', 'ZTE', 'LG', 'dazen',\
              'Nokia', 'AMOI', 'Meizu', 'sony', 'GT-', 'SM-', 'SCH-', \
              'TCL', 'ASUS', 'Hisense', 'Changhong', 'MX', 'Macintosh', 'Windows NT']
    for brand in brands:
        if brand in str(string):
            return brand
    return 'others'

def brand_trans(data):
    '''品牌转换'''
    iPhone = ['iPhone 4', 'iPhone 4s', 'iPhone 5', 'iPhone 5s', 'iPhone 5c', \
              'iPhone 6', 'iPhone 6p', 'iPhone 6s', 'iPhone 6sp']
    SAMSUNG = ['GT-', 'SM-', 'SCH-']
    Meizu = ['MX']
    HUAWEI = ['HONOR']
    if data in iPhone:
        return 'iPhone'
    elif data in SAMSUNG:
        return 'SAMSUNG'
    elif data in Meizu:
        return 'Meizu'
    elif data in HUAWEI:
        return 'HUAWEI'
    else:
        return data

def brand_count(data, n):
    '''计算总和超过n的最小品牌数'''
    result = []
    count = collections.Counter(data)
    length = len(data)
    for each in count:
        if str(each) != 'others':
            p = int(count[each]) * 1.0 / length
            result.append(p)
    result.sort(reverse = True)
    sum_proportion = 0
    brand_n = 0
    for each in result:
        if sum_proportion > float(n):
            return brand_n
        else:
            sum_proportion += each
            brand_n += 1
    return 0
    
def brand_var(data):
    '''计算各品牌所占比例的方差'''
    ratio_list = []
    count = collections.Counter(data)
    ent = 0
    length = len(data)
    for each in count:
        p = int(count[each]) * 1.0 / length
        ratio_list.append(p)
    return var(ratio_list)

def test():
    data = ['iPhone 4', 'SM-', 'SAMSUNG']
    print data
    print brand_trans(data)


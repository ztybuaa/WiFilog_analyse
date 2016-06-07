#-*- coding: utf-8 -*-
"""interval_time"""

import collections
from numpy import var, log2

def entropy(data):
    '''计算列表信息熵'''
    collection = collections.Counter(data)
    ent = 0
    length = len(data)
    for each in collection:
        p = collection[each] * 1.0 / length
        if p > 0:
            ent -= p * log2(p)
    return ent

def nearby_difference_list(data):
    '''返回相邻元素相减后的列表'''
    result = []
    length = len(data)
    for num in range(1,length):
        result.append(int(data[num]) - int(data[num-1]))
    return result

def test():
    data = [1, 2, 4, 1, 2, 1]
    print data
    print entropy(data)


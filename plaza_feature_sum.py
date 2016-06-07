#-*- coding: utf-8 -*-
"""plaza_feature_sum"""

import string
import csv
import time

READ_PATH = r'result/plaza_feature.csv'
SAVE_PATH = r'result/plaza_feature_sum.csv'
N = 3 #days

def plaza_feature_sum(name):
    result = {}
    reader = csv.reader(open(name, 'rb'))
    for line in reader:
        if str(line[1]) != 'brand_var':
            plaza = str(line[0])
            try:
                if plaza not in result.keys():
                    result[plaza] = {}
                    result[plaza]['brand_var'] = []
                    result[plaza]['average_login_time'] = []
                    result[plaza]['var_login_time'] = []
                    result[plaza]['average_nearby_time'] = []
                    result[plaza]['entropy_nearby_time'] = []
                    result[plaza]['brand_proportion0.5'] = []
                    result[plaza]['brand_var'].append(float(line[1]))
                    result[plaza]['average_login_time'].append(float(line[2]))
                    result[plaza]['var_login_time'].append(float(line[3]))
                    result[plaza]['average_nearby_time'].append(float(line[4]))
                    result[plaza]['entropy_nearby_time'].append(float(line[5]))
                    result[plaza]['brand_proportion0.5'].append(float(line[6]))
                else:
                    result[plaza]['brand_var'].append(float(line[1]))
                    result[plaza]['average_login_time'].append(float(line[2]))
                    result[plaza]['var_login_time'].append(float(line[3]))
                    result[plaza]['average_nearby_time'].append(float(line[4]))
                    result[plaza]['entropy_nearby_time'].append(float(line[5]))
                    result[plaza]['brand_proportion0.5'].append(float(line[6]))
            except Exception,e:
                print e

    for plaza in result:
        if len(result[plaza]['brand_var']) == N:
            result[plaza]['b_v'] = sum(result[plaza]['brand_var']) * 1.0 / N
        else:
            result[plaza]['b_v'] = ''            
        if len(result[plaza]['average_login_time']) == N:
            result[plaza]['a_l_t'] = sum(result[plaza]['average_login_time']) * 1.0 / N
        else:
            result[plaza]['a_l_t'] = ''
        if len(result[plaza]['var_login_time']) == N:
            result[plaza]['v_l_t'] = sum(result[plaza]['var_login_time']) * 1.0 / N
        else:
            result[plaza]['v_l_t'] = ''
        if len(result[plaza]['average_nearby_time']) == N:
            result[plaza]['a_n_t'] = sum(result[plaza]['average_nearby_time']) * 1.0 / N
        else:
            result[plaza]['a_n_t'] = ''
        if len(result[plaza]['entropy_nearby_time']) == N:
            result[plaza]['e_n_t'] = sum(result[plaza]['entropy_nearby_time']) * 1.0 / N
        else:
            result[plaza]['e_n_t'] = ''
        if len(result[plaza]['brand_proportion0.5']) == N:
            result[plaza]['b_p_5'] = sum(result[plaza]['brand_proportion0.5']) * 1.0 / N
        else:
            result[plaza]['b_p_5'] = ''
         
    with open(SAVE_PATH, 'ab') as f:
        writer = csv.writer(f)
        writer.writerow(['plaza_id','brand_var', 'average_login_time', 'var_login_time', \
                         'average_nearby_time', 'entropy_nearby_time', \
                         'brand_proportion0.5'])
        for plaza in result:
            line = []
            line.append(plaza)
            line.append(result[plaza]['b_v'])
            line.append(result[plaza]['a_l_t'])
            line.append(result[plaza]['v_l_t'])
            line.append(result[plaza]['a_n_t'])
            line.append(result[plaza]['e_n_t'])
            line.append(result[plaza]['b_p_5'])
            writer.writerow(line)
        f.close()        

if __name__ == '__main__':
    print 'starting...'
    t_start = time.time()
    plaza_feature_sum(READ_PATH)
    t_end = time.time()
    print 'cost %f sec' % (t_end - t_start)
    print 'ending...'

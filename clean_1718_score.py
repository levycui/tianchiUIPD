#!/usr/bin/env python
# -*- coding:UTF-8 -*-
#run python getscore.py ans.csv
import sys
#把第30天的对象单独写入offline_groundtruth.txt
#读出全部数据
st = open('./offline_groundtruth.txt')
const = st.readlines()

answer = []
for a in const:
    if a[0] == 'u':
        continue
    answer.append(a)
answer = set(answer)

#把生成的答案读取出来
#f = open(sys.argv[1])
f = open('./tianchi_mobile_recommendation_predict_old.csv')
con = f.readlines()
you = []
for a in con:
    if a[0] == 'u':
        continue
    you.append(a)
you = set(you)

#取交集
inter = answer & you

print 'hit number = ', len(inter)

#使用评估算法计算F1/P/R数值
if len(inter) > 0:
    a = len(answer)
    b = len(you)
    c = len(inter)
    R = 1.0 * c / a * 100
    P = 1.0 * c / b * 100
    F1 = 2.0 * R * P / (R + P)
    print 'F1/P/R %.2f%%/%.2f%%/%.2f%%\n' %(F1, P, R)

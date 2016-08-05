#!/usr/bin/env python
# -*- coding:UTF-8 -*-
# 清洗用户购买数据，将一个月的历史记录，用户购买的物品求平均值，保留平均值以上的用户
# 浏览、收藏、加购物车、购买，对应取值分别是1、2、3、4
data = open('/home/levy/PycharmProjects/tianchi/UIPD/clean_user.csv')
context = data.readlines()
train_data = []
for line in context:
    line = line.replace('\n','')
    line = line.replace('\r','')
    array = line.split(',')
    if array[0] == 'user_id':
        continue
    type = array[2]
    #print type
    if type == '4':
        uid = (array[0],array[1],array[2],array[-1])
        train_data.append(uid)
print len(train_data)
print train_data[:20]

#将结果写入到文件中
wf = open('clean_user_bug.csv','w')
wf.write('user_id,item_id,behavior_type,time\n')
for i in range(len(train_data)):
    item = train_data[i]
    wf.write('%s,%s,%s,%s\n'%(item))
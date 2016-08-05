#!/usr/bin/env python
# -*- coding:UTF-8 -*-

data = open('/root/PycharmProjects/UIPD/tianchi_fresh_comp_train_user.csv')
#clean_user_test_date.csv
#tianchi_fresh_comp_train_user.csv
context = data.readlines()
train_data = []
for line in context:
    #将回车换掉
    line = line.replace('\n','')
    line = line.replace('\r','')
    #使用逗号进行分割
    array = line.split(',')
    #过滤第一行
    if array[0] =='user_id':
        continue
    #生成item 候选对象
    #过滤2014-11-18日期的数据
    if array[-1][5:10] == '11-18':
        continue
    uid = (array[0],array[1],array[2],array[-1][8:10])
    train_data.append(uid)
print len(train_data)
print train_data[:10]

#将结果写入到文件中
wf = open('clean_user_new.csv','w')
#wf = open('clean_user_test.csv','w')

wf.write('user_id,item_id,behavior_type,time\n')
for i in range(len(train_data)):
    item = train_data[i]
    wf.write('%s,%s,%s,%s\n'%(item))
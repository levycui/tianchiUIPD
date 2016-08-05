#!/usr/bin/env python
# -*- coding:UTF-8 -*-

data = open('./tianchi_fresh_comp_train_user.csv')
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
    #取出日期为18号的数据
    if array[2]=='4' and array[-1][8:10] =='18':
        uid = (array[0],array[1])
        train_data.append(uid)
print len(train_data)
print train_data[:10]

#将结果写入到文件中
wf = open('offline_groundtruth.txt','w')
#wf = open('clean_user_test.csv','w')

wf.write('user_id,item_id\n')
for i in range(len(train_data)):
    item = train_data[i]
    #写入数据的格式
    wf.write('%s,%s\n'%(item))
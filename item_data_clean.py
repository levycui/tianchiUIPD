#!/usr/bin/env python
# -*- coding:UTF-8 -*-

data = open('/home/levy/PycharmProjects/tianchi/UIPD/tianchi_fresh_comp_train_item.csv')
context = data.readlines()
train_data = []
for line in context:
    #将回车换掉
    line = line.replace('\n','')
    line = line.replace('\r','')
    #使用逗号进行分割
    array = line.split(',')
    #过滤第一行
    if array[0] =='item_id':
        continue
    #生成item 候选对象
    uid = (array[0],array[-1])
    train_data.append(uid)
print len(train_data)
print train_data[:10]

#将结果写入到文件中
wf = open('clean_item.csv','w')
wf.write('item_id,item_category\n')
for i in range(len(train_data)):
    item = train_data[i]
    wf.write('%s,%s\n'%(item))
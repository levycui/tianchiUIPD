#!/usr/bin/env python
# -*- coding:UTF-8 -*-

# run python implus.py

# 导入数据
f = open('/root/PycharmProjects/UIPD/clean_user_new.csv')
# 将没一行放入context中
context = f.readlines()
# 导入import
import numpy as np

# 取训练数据包含了抽样出来的一定量用户在一个月时间（11.18~12.18）之内的移动端行为数据（D），
# 评分数据是这些用户在这个一个月之后的一天（12.19）对商品子集（P）的购买数据。

train_day17 = []
offline_candidate_day18 = []
online_candidate_day19 = []
# 循环读取每一行
for line in context:
    # 将回车换掉
    line = line.replace('\n', '')
    # 使用逗号进行分割
    array = line.split(',')
    # 过滤第一行
    if array[0] == 'user_id':
        continue
    # int表示最后一天
    day = int(array[-1])

    # 生成UID 候选对象
    uid = (array[0], array[1], day + 1)
    if day == 18:
        train_day17.append(uid)
    if day == 19:
        offline_candidate_day18.append(uid)
    if day == 20:
        online_candidate_day19.append(uid)

# 处理重复对象 去重
train_day17 = list(set(train_day17))
offline_candidate_day18 = list(set(offline_candidate_day18))
online_candidate_day19 = list(set(online_candidate_day19))

# 显示数据量
print 'training item number:\t', len(train_day17)
# print train_day17
print '----------------------\n'
print 'offline candidate item number:\t', len(offline_candidate_day18)
# print offline_candidate_day18
print '----------------------\n'

import math

# 特征统计
# 生成4个不同映射表
ui_dict = [{} for i in range(4)]
# 读取每一行
for line in context:
    line = line.replace('\n', '')
    array = line.split(',')
    # 过滤第一行
    if array[0] == 'user_id':
        continue
    # 得到最后一天作为日期
    day = int(array[-1])
    # 得到所有数据的3元组
    uid = (array[0], array[1], day)
    #
    type = int(array[2]) - 1
    # 将3元组统计到对应的类型中
    if uid in ui_dict[type]:
        ui_dict[type][uid] += 1
    else:
        ui_dict[type][uid] = 1

# print ui_dict[:10]
# print '-------------------------\n'

#打标签
ui_buy = {}
for line in context:
    line = line.replace('\n', '')
    array = line.split(',')
    if array[0] == 'user_id':
        continue
    uid = (array[0], array[1], int(array[-1]))
    # 操作为4的（购买）打个标签
    if array[2] == '4':
        ui_buy[uid] = 1



# 对训练样本 X ,y  生成特征向量和样本标签
# 定义矩阵
X = np.zeros((len(train_day17), 4))
y = np.zeros((len(train_day17)), )
# print X
# print y
# print '-------------------------\n'
id = 0
# 把这里train_day17的列表数据拿出来
for uid in train_day17:
    # 统计前一天所有的浏览次数
    last_uid = (uid[0], uid[1], uid[2] - 1)
    # 按顺序统计4种类型的数量，不存在之前的映射表中设置为0
    for i in range(4):
        X[id][i] = math.log1p(ui_dict[i][last_uid] if last_uid in ui_dict[i] else 0)
    # 标签存在之前的列表中为1，不存在为0
    y[id] = 1 if uid in ui_buy else 0
    id += 1
# 打印出特征向量和标签
print 'X = ', X, '\n\n', 'y = ', y
print '-----------------------\n\n'
print 'train number = ', len(y), 'positive number = ', sum(y), '\n'

# get predict px for offline_candidate_day18
pX = np.zeros((len(offline_candidate_day18),4))
id = 0
for uid in offline_candidate_day18:

    last_uid= (uid[0],uid[1],uid[2]-1)
    for i in range(4):
        pX[id][i] = math.log1p(ui_dict[i][last_uid] if last_uid in ui_dict[i] else 0)
    id +=1


#训练模型
#调用模型逻辑回归
from sklearn.linear_model import LogisticRegression
#定义模型，使用默认的超参数
model = LogisticRegression()
#训练数据
model.fit(X,y)

#预测评估
py = model.predict_proba(pX)
npy = []
#把属于1的概来
for a in py:
    npy.append(a[1])
py = npy

print 'pX ='
print pX
#
# #combine 把概率和原始对象打包
# lx =zip(offline_candidate_day18,py)
# print '------------'
# #sort by predict score
# #把置信度大的排在前面 从大到小
# lx = sorted(lx,key = lambda x:x[1],reverse=True)
# print '------------'
# #将结果写入到文件中
# wf = open('tianchi_mobile_recommendation_predict.csv','w')
# wf.write('user_id,item_id\n')
# #提交437个测试
# for i in range(30000):
# #for i in range(len(offline_candidate_day18)):
#     item = lx[i]
#     wf.write('%s,%s\n'%(item[0][0],item[0][1]))

# -*- coding:UTF-8 -*-
from numpy import *
from math import log
import operator
import time
import ConfigParser
import os

#µ½ÎÄ¼þÖÐ²éÕÒÍ£ÓÃ´Ê
def get_stop_words():
    #»ñÈ¡µ±Ç°Â·¾¶
    path = os.getcwd()
    #µ¼ÈëÅäÖÃÎÄ¼þ
    conf = ConfigParser.ConfigParser()
    conf.read("setting.conf")
    #ÎÄ¼þÂ·¾¶
    #´æ·ÅÍ£ÓÃ´ÊµÄÎÄ¼þµÄÂ·¾¶¡£
    stopWordsFile = os.path.join(path,os.path.normpath(conf.get("filepath", "stopWordsFile")))
    #´æ·ÅÍ£ÓÃ´ÊµÄset
    s = set()
    #´ò¿ªÍ£ÓÃ´ÊÎÄ¼þ¡£
    fr = open(stopWordsFile)
    for line in fr.readlines():#¶ÁÃ¿Ò»ÐÐ
        sublist=line.strip().split('\t')#É¾³ýÕâÒ»ÐÐÍ·Î²¿Õ°×,²¢·Ö³Élist
        for w in sublist:
            s.add(w.strip())
        # s.update(sublist)
    fr.close()
    return s

if __name__=='__main__':
    s = set()
    # s=([1,2,3])
    # print (1 in s)  #´òÓ¡True
    # s = (['a','b','c'])
    # print ('a' in s) #´òÓ¡True
    # s = (['ËÆµÄ','µãµã'])
    # print ('ËÆµÄ' in s) #´òÓ¡True
    s = get_stop_words()
    print ('ËÆµÄ' in s)
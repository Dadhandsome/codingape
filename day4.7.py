# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 15:23:26 2021

@author: User
"""

from random import randrange
from time import time
def linearsearch():
    sTime=time()
    for i in range(1,10000001):
        if i==number:
            print("找到了!是"+str(i))
            print("花了"+str(time()-sTime)+"秒")
            break
number=randrange(1,10000001)
linearsearch()

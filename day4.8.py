# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 16:08:51 2021

@author: User
"""

from random import randrange
from time import time
def binarysearch():
    sTime=time()
    low=0
    top=10000000
    while low<=top:
        mid=(low+top)//2
        if mid<number:
            low=mid+1
        elif mid>number:
            top=mid-1
        else:
            print("找到了!是"+str(mid))
            print("花了"+str(time()-sTime)+"秒")
            break
number=randrange(1,10000001)
binarysearch()

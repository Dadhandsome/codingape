# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 14:29:08 2021

@author: User
"""

from mcpi.minecraft import Minecraft
from random import randrange
mc=Minecraft.create()
r=randrange(0,16)
while True:
    hits=mc.events.pollBlockHits()
    if len (hits)>0:
        hit=hits[0]
        block=mc.getBlockWithData(hit.pos)
        data=block.data
        if data==r:
            mc.postTochat("恭喜您找到我ovo")
            mc.setBlocks(hit.pos,57) 
            break
        elif data<r:
            mc.postToChat("錯!要大一點")
        elif data>r:
            mc.postToChat("錯!在小一點")
            
    
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 10:23:16 2021

@author: User
"""

    color=random.randint(0,16)
mc=Minecraft.create()import time
import random
from mcpi.minecraft import Minecraft
while True:
    x,y,z=mc.player.getTilePos()
    mc.setBlocks(x-25,y-1,z-25,x+25,y-1,z+25,95,color)
    time.sleep(0.5)
    
    
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 11:36:55 2021

@author: User
"""

import time
import random
from mcpi.minecraft import Minecraft
mc=Minecraft.create()
count=0
while count<50:
    x,y,z=mc.player.getTilePos()
    color=random.randrange(0,9)
    mc.setBlock(x,y,z,38,color)
    time.sleep(0.2)
    count=count+1
     
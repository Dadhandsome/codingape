# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 10:25:02 2021

@author: User
"""

from mcpi.minecraft import Minecraft
import random
import time
mc=Minecraft.create()
while True:
    x,y,z=mc.player.getPos()
    x=x+random.uniform(-20,20)
    z=z+random.uniform(-20,20)
    y=y+30
    mc.spawnEntity(x,y,z,98)
    time.sleep(0.2)
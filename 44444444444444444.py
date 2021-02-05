# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 11:17:32 2021

@author: User
"""

import time
from mcpi.minecraft import Minecraft
mc=Minecraft.create()
while True:
    x,y,z=mc.player.getTilePos()
    mc.setBlock(x,y,z,38)
    time.sleep(0.2)
    
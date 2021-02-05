# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 11:43:16 2021

@author: User
"""

from mcpi.minecraft import Minecraft
mc=Minecraft.create()
x,y,z=mc.player.getTilePos()
for q in range(20):
    mc.setBlock(x,y-1,z+q,46)
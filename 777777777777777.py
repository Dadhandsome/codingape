# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 14:55:12 2021

@author: User
"""

from mcpi.minecraft import Minecraft
mc=Minecraft.create()
x,y,z=mc.player.getTilePos()
a=0
while a<10:
     mc.setBlocks(x-30,y-1,z,x+30,y-10,z,19)
     z=z-5
     a=a+1
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 09:25:32 2021

@author: User
"""

from mcpi.minecraft import Minecraft
mc=Minecraft.create()
x,y,z=mc.player.getTilePos()

mc.setBlocks(x-1,y-1,z-1,x+1,y-1,z+1,11)
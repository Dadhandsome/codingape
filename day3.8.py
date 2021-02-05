# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 11:58:54 2021

@author: User
"""

from mcpi.minecraft import Minecraft
mc=Minecraft.create()
x,y,z=mc.player.getTilePos()
x,y,z=mc.player.getTilePos()(20):
    mc.setBlock(x+q,y-1,z+q,46)
    mc.setBlock(x+q-1,y-1,z+q,46)
    mc.setBlock(x+q+1,y-1,z+q,46)
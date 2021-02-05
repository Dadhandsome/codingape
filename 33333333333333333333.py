# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 10:44:48 2021

@author: User
"""



from mcpi.minecraft import Minecraft
mc=Minecraft.create()
x,y,z=mc.player.getTilePos()
a=6
b=6
c=8
mc.setBlocks(x,y,z,x+a,y+b,z+c,46)
mc.setBlocks(x+1,y+1,z+1,x+a-1,y+b-1,z+c-1,0)
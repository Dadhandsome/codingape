# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 15:18:58 2021

@author: User
"""

from mcpi.minecraft import Minecraft
mc=Minecraft.create()
x,y,z=mc.player.getTilePos()
try:
    blockType=int(input("輸入你要的方塊ID:")
    mc.setBlock(x,y,z,blockType)
except:
    print("只能輸入數字!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
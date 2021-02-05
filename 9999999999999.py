# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 16:07:27 2021

@author: User
"""

from mcpi.minecraft import Minecraft
mc=Minecraft.create()
x,y,z=mc.player.getTilePos()
mc.setSign(x+1,y,z,63,2,9,4,5,3)
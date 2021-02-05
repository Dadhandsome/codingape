# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 14:03:05 2021

@author: User
"""

from mcpi.minecraft import Minecraft
mc= Minecraft.create()
x=248.857
y=76
z=255.678
mc.player.setPos(x,y,z)
time.sieep(0.5)y=y+1
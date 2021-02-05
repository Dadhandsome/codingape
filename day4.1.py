# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 09:16:24 2021

@author: User
"""

from mcpi.minecraft import Minecraft
mc=Minecraft.create()
a=[]
b=[]
c=[]
for i in range(1,4):
    a.append(1*i)
    b.append(2*i)
    c.append(3*i)
x,y,z=mc.player.getTilePos()
mc.setSign(x,y,z,63,0,str(a),str(b),str(c))
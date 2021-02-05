# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 16:15:19 2021

@author: User
"""

from mcpi.minecraft import Minecraft
mc=Minecraft.create()
x,y,z=mc.player.getTilePos()
mc.setBlock(x,y,z,46)
mc.setBlock(x,y+1,z,46)
mc.setBlock(x,y+2,z,46)
mc.setBlock(x,y+3,z,46)
mc.setBlock(x,y+4,z,46)
mc.setBlock(x,y+5,z,46)
mc.setBlock(x,y+6,z,46)
mc.setBlock(x,y+7,z,46)
mc.setBlock(x,y+8,z,46)
mc.setBlock(x,y+9,z,46)
mc.setBlock(x,y+10,z,46)
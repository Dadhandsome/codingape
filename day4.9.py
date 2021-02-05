# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 16:38:36 2021

@author: User
"""

from mcpi.minecraft import Minecraft
mc=Minecraft.create()
myID=mc.getPlayerEntityId("Dadhandsome")
mc.postToTitle(myID,"Hello")
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 09:59:20 2021

@author: User
"""

import random
from mcpi.minecraft import Minecraft
mc=Minecraft.create()
color=random.randrange(0,16)
mc.setBlocks(x-25,y-1,z-25,x+25,y-1,z+25,57,color)

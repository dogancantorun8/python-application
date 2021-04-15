# -*- coding: utf-8 -*-
"""
Created on Sun Mar 28 17:25:22 2021

@author: Asus
"""


##Pythonda getter setter yazmak istersem
import math

class Circle:
    def __init__(self, radius):
        self.radius = radius
                
    def area(self):
        return self.radius ** 2 * math.pi
    
    def setArea(self, area):
        self.radius = math.sqrt(area / math.pi)
        
c = Circle(10)
print(c.radius)
print(c.area())

c.setArea(1)
print(c.radius)
print(c.area())

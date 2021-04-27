# -*- coding: utf-8 -*-
"""
Created on Sat Apr 17 18:34:08 2021

@author: dogancan
"""

##Hiç bir xml dosyasından okuma yapmadan manuel girisle olusturdugumuz XMl'i yeni bir dosyay yazma

import xml.etree.ElementTree as ET

fruits = ET.Element('fruits', {'a': '123', 'b': '566'})

apple = ET.Element('apple')
apple.text = '12'
fruits.append(apple)

banana = ET.Element('banana')
banana.text = '23'
fruits.append(banana)
ET.dump(fruits)

print('---------------------------')
        
for e in fruits.iter():
    print(e.tag, e.text)
    
print('---------------------------')
    
se = ET.SubElement(fruits, 'cherry')
se.text = '34'
ET.dump(fruits)

et = ET.ElementTree(fruits)
et.write('fruits.xml')


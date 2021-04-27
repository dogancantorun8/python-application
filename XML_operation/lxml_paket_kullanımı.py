# -*- coding: utf-8 -*-
"""
Created on Sat Apr 17 18:39:19 2021

@author: dogancan torun
"""


#lxml third part paket yardımıyla xml parse işlemi (standart kütüphane içerisinde yer almaz) 
import lxml.etree as ET

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

print('------------------------------------')
ET.tostring(fruits, pretty_print=True)


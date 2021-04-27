# -*- coding: utf-8 -*-
"""
Created on Sat Apr 17 17:46:59 2021

@author: dogancan 

"""

#Kendi xmlimizi oluşturmak istersek;
import xml.etree.ElementTree as ET

root = ET.Element('root', {'a': '123', 'b': '566'}, text='this is a test')

ET.dump(root)

 
#Root elemana eklemeler yapmak istersem; fruits taginin içerisine apple ve banana ekliyorum 
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

##dump ile elde edilen XML ağacının gösterilmesi için yapılır 
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
se.text = 'cherry'
ET.dump(fruits)
    
